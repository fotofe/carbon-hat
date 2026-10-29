#!/usr/bin/env python3
"""Make Carbon hat's textures and wallpapers.

Every texture is a small pixel-art tile that repeats. Bigger copies are
made with nearest-neighbour scaling so the pixels stay sharp.

    python3 tools/make_textures.py
"""
import math
import random
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
TEX = ROOT / "system_files/usr/share/carbonhat/textures"
WALL = ROOT / "system_files/usr/share/wallpapers/CarbonHat/contents"

SCALES = (1, 2, 3)
# Cog levels: cog 1 sits at the bottom and is the lightest; every cog
# stacked on top of it is one step darker.
CARBON_LEVELS = {"carbon-1": 18, "carbon-2": 9, "carbon-3": 0}
LINEN_LEVELS = {"linen-1": 0, "linen-2": -8, "linen-3": -16}
WALL_SIZES = ((1366, 768), (1920, 1080), (1920, 1200),
              (2560, 1440), (2560, 1600), (3840, 2160))
FEDORA_BLUE = (53, 132, 228)


def carbon_tile():
    """The user's own 16x16 carbon fibre tile, unchanged."""
    return Image.open(ROOT / "art/carbon-source.png").convert("RGB")


def linen_tile(size=32, seed=44):
    """Plain weave with 2 px threads. Each thread gets a small fixed tone
    offset so it reads as linen, not graph paper."""
    rnd = random.Random(seed)
    n = size // 2
    row_tone = [rnd.choice((-3, -2, 0, 0, 1, 3)) for _ in range(n)]
    col_tone = [rnd.choice((-3, -2, 0, 0, 1, 3)) for _ in range(n)]
    base = (236, 231, 220)
    img = Image.new("RGB", (size, size))
    px = img.load()
    for y in range(size):
        for x in range(size):
            i, j = y // 2, x // 2
            if (i + j) % 2 == 0:   # horizontal thread on top
                shade = (5 if y % 2 == 0 else -4) + row_tone[i]
            else:                  # vertical thread on top
                shade = (3 if x % 2 == 0 else -6) + col_tone[j]
            px[x, y] = tuple(max(0, min(255, c + shade)) for c in base)
    return img


def shift(img, amount):
    return img.point(lambda v: max(0, min(255, v + amount)))


def scaled(img, k):
    return img.resize((img.width * k, img.height * k), Image.NEAREST)


def radial_mask(size, cx, cy, radius, strength, invert=False):
    """Smooth round mask, drawn small and scaled up (it has no detail)."""
    sw, sh = 96, 54
    small = Image.new("L", (sw, sh))
    px = small.load()
    for y in range(sh):
        for x in range(sw):
            d = math.hypot((x / sw - cx) * 16 / 9, y / sh - cy) / radius
            t = max(0.0, 1.0 - d) if not invert else min(1.0, d)
            px[x, y] = int(255 * strength * t * t)
    return small.resize(size, Image.BICUBIC)


def wallpaper(tile, size, glow, shade, dark):
    w, h = size
    big = scaled(tile, max(1, round(h / 540)))
    img = Image.new("RGB", size)
    for y in range(0, h, big.height):
        for x in range(0, w, big.width):
            img.paste(big, (x, y))
    img = Image.composite(Image.new("RGB", size, glow), img,
                          radial_mask(size, 0.5, 0.0, 0.9, 0.22 if dark else 0.45))
    return Image.composite(Image.new("RGB", size, shade), img,
                           radial_mask(size, 0.5, 0.5, 1.1, 0.35 if dark else 0.2, invert=True))


def main():
    TEX.mkdir(parents=True, exist_ok=True)
    carbon, linen = carbon_tile(), linen_tile()
    sheet = []
    for levels, tile in ((CARBON_LEVELS, carbon), (LINEN_LEVELS, linen)):
        for name, amount in levels.items():
            level = shift(tile, amount)
            sheet.append(level)
            for k in SCALES:
                suffix = "" if k == 1 else f"@{k}x"
                scaled(level, k).save(TEX / f"{name}{suffix}.png", optimize=True)

    for folder, tile, glow, shade, dark in (
            ("images_dark", carbon, FEDORA_BLUE, (0, 0, 0), True),
            ("images", linen, (255, 251, 242), (196, 186, 170), False)):
        (WALL / folder).mkdir(parents=True, exist_ok=True)
        for size in WALL_SIZES:
            wallpaper(tile, size, glow, shade, dark).save(
                WALL / folder / f"{size[0]}x{size[1]}.png", optimize=True)

    # Preview sheet for people, not shipped: every level at 8x, side by side.
    cell = 32 * 8
    preview = Image.new("RGB", (cell * 3, cell * 2), (128, 128, 128))
    for n, level in enumerate(sheet):
        big = scaled(level, 8)
        for y in range(0, cell, big.height):
            for x in range(0, cell, big.width):
                preview.paste(big, ((n % 3) * cell + x, (n // 3) * cell + y))
    preview.save(ROOT / "art/texture-preview.png")


if __name__ == "__main__":
    main()
