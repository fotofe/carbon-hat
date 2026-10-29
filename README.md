# Carbon hat

A Fedora 44 Atomic desktop with KDE Plasma, carbon fibre and linen textures, a
cog app launcher and no-terminal-needed defaults. See [PLAN.md](PLAN.md).

**Status:** early. The system image builds, but there is no installer yet.

## How it is built

GitHub builds the image from [Containerfile](Containerfile) every time something
is pushed, and once a day to pick up Fedora updates. The image is published at
`ghcr.io/fotofe/carbon-hat`.

| Folder | What's in it |
|--------|--------------|
| `build/` | Script that runs inside the image build |
| `system_files/` | Files copied into the system as-is |
| `tools/` | Generators for textures, wallpapers and colour schemes |
| `art/` | Source art (`carbon-source.png`) and previews |

Changing the textures or colours: edit `tools/make_textures.py` or
`tools/make_colors.py`, run it, and commit the files it writes.
