#!/usr/bin/env python3
"""Write Carbon hat's KDE colour schemes (dark = carbon, light = linen).

Flat colours are what apps fall back to where a texture can't be drawn,
so each one matches the average tone of its texture.

    python3 tools/make_colors.py
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "system_files/usr/share/color-schemes"

SCHEMES = {
    "CarbonHatDark": dict(
        name="Carbon hat Dark",
        window="22,22,22", view="18,18,18", button="42,42,42", header="14,14,14",
        alt_view="26,26,26", text="242,242,242", dim="154,154,154",
        accent="53,132,228", on_accent="255,255,255",
        link="120,174,237", visited="192,97,203",
        negative="255,123,99", neutral="248,228,92", positive="87,227,137",
        tooltip="34,34,34",
    ),
    "CarbonHatLight": dict(
        name="Carbon hat Light",
        window="236,231,220", view="247,244,238", button="224,218,206", header="228,223,211",
        alt_view="240,236,228", text="43,38,34", dim="111,103,93",
        accent="28,113,216", on_accent="255,255,255",
        link="28,113,216", visited="129,61,156",
        negative="192,28,40", neutral="156,110,3", positive="38,162,105",
        tooltip="250,248,243",
    ),
}


def color_set(p, bg, fg=None, alt=None):
    fg = fg or p["text"]
    return {
        "BackgroundNormal": bg,
        "BackgroundAlternate": alt or bg,
        "ForegroundNormal": fg,
        "ForegroundInactive": p["dim"] if fg == p["text"] else fg,
        "ForegroundActive": p["accent"] if fg == p["text"] else fg,
        "ForegroundLink": p["link"],
        "ForegroundVisited": p["visited"],
        "ForegroundNegative": p["negative"],
        "ForegroundNeutral": p["neutral"],
        "ForegroundPositive": p["positive"],
        "DecorationFocus": p["accent"],
        "DecorationHover": p["accent"],
    }


def scheme(key, p):
    groups = {
        "Colors:Window": color_set(p, p["window"]),
        "Colors:View": color_set(p, p["view"], alt=p["alt_view"]),
        "Colors:Button": color_set(p, p["button"]),
        "Colors:Header": color_set(p, p["header"]),
        "Colors:Header][Inactive": color_set(p, p["window"]),
        "Colors:Selection": color_set(p, p["accent"], fg=p["on_accent"]),
        "Colors:Tooltip": color_set(p, p["tooltip"]),
        # Panels, cogs and the dock are always dark, like the carbon.
        "Colors:Complementary": color_set(SCHEMES["CarbonHatDark"], "22,22,22"),
        "General": {"ColorScheme": key, "Name": p["name"], "shadeSortColumn": "true"},
        "KDE": {"contrast": "4"},
        "WM": {
            "activeBackground": p["header"], "activeForeground": p["text"],
            "activeBlend": p["text"],
            "inactiveBackground": p["window"], "inactiveForeground": p["dim"],
            "inactiveBlend": p["dim"],
        },
    }
    lines = []
    for group, keys in groups.items():
        lines.append(f"[{group}]")
        lines += [f"{k}={v}" for k, v in keys.items()]
        lines.append("")
    return "\n".join(lines)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for key, palette in SCHEMES.items():
        (OUT / f"{key}.colors").write_text(scheme(key, palette))


if __name__ == "__main__":
    main()
