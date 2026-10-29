# Carbon hat plan

Progress tracker for Carbon hat. ✅ done · 🔨 in progress · ⬜ not started.
"Session" = one working conversation with Claude.

| # | Phase | Status | Estimate |
|---|-------|--------|----------|
| 0 | Build pipeline, base image, codecs, memory tuning, textures, colours, wallpapers, file.txt | ✅ | 1 session |
| 1 | Installer ISO + first test on a USB stick / spare PC | 🔨 (ISO workflow added; not yet tested) | 1–2 sessions |
| 2 | Look: textured panels and menus, app style, window borders, GTK colours, login screen, boot logo | ⬜ | 2–3 sessions |
| 3 | Shell: bottom white bar + hover dock, top bar (only in apps), home screen clock + widgets, Right Alt overview | ⬜ | 3–4 sessions |
| 4 | Cogs: Super ×1/×2/×3, Ctrl+Super, categories (auto-detect, merge, custom) | ⬜ | 2–3 sessions |
| 5 | Super Look (Super+S) | ⬜ | 1–2 sessions |
| 6 | Power modes + speed: CachyOS kernel, active-app priority, adaptive effects | ⬜ | 2 sessions |
| 7 | Store app (Flathub, page per app, Install/Remove) | ⬜ | 3–4 sessions |
| 8 | Apps: symbol, tick, Tophat, Features, What's new, System category | ⬜ | 4–6 sessions |
| 9 | First-boot setup: GPU question, printers + Wi-Fi printing, app bundles, cog categories, tutorial; update notifications | ⬜ | 3–4 sessions |

## What Carbon hat is

**Base:** Fedora 44 Atomic with KDE Plasma 6 (Kinoite), built on GitHub. The whole system updates at once and can roll back. It looks like Fedora 44 Workstation (GNOME-style), but runs on KDE.

**Textures:** every surface is a small pixel-art tile that repeats.
- Dark mode is carbon fibre (`art/carbon-source.png`, the user's own tile).
- Light mode is a linen weave.
- Cogs stack from lightest (cog 1, at the bottom) to darkest (top). Pixels are scaled without smoothing.
- Animations must stay smooth on slow PCs.

**Home screen:**
- With no windows open, the screen looks like the iOS lock screen: a big clock, with seconds as a setting.
- Below the clock are now-playing widgets for music and YouTube, plus weather, timers and workspaces.

**Top bar:**
- It only appears while an app is open.
- It holds media controls, weather + calendar, workspaces + clipboard history, and timers.
- It also holds the power mode switch.

**Bottom bar and dock:**
- A thin white bar sits at the bottom. Its position can be changed in Settings.
- Hovering over it shows the dock with your pinned apps and a ⋮⋮⋮ button that opens all apps.

**Cogs (app launcher):**
- Super ×1, ×2 and ×3 slide in cog 1 from the right, then cog 2 from the left, then cog 3 from the right. Each cog stacks on the previous one.
- Ctrl+Super opens all three at once.
- Cogs hold app categories. Categories are detected automatically, and you can create and merge your own.
- In setup, the user orders the categories and drags them onto each cog.

**Keys:**
- Right Alt opens the window overview.
- Super+Tab switches apps quickly.
- Super+S opens Super Look. Every key can be changed in Settings.

**Super Look:** apps and settings, files, math, units and time, plus quick web answers.

**Power modes:** Performance, Balance and Battery. Balance has a manual switch between "Performance on battery" and "Gaming".

**Speed and memory:**
- The CachyOS (BORE) kernel.
- zram sized by RAM ✅
- Effects that adapt to the GPU.
- CPU priority for the app you're using.

**Store:** our own Flathub app. Every app gets its own page with an Install or Remove button.

**Apps:**
- **symbol**: emoji and special characters, pasted straight into what you're typing.
- **tick**: quick alarms.
- **Tophat**: views every file format, including unknown ones (as hex and text). Pixel art stays sharp.
- **Features**: explains what the OS can do.
- **What's new**: shows what changed in each version.
- **System category**: a system monitor and similar tools.
- **Files**: right-click → New → file.txt ✅

**Setup (first boot):**
- Asks "Do you have an NVIDIA GPU?" with three answers: Yes / No, AMD / No, integrated.
- Printer: you pick your model, the driver installs, and Wi-Fi printing gets set up.
- App bundles to pick from.
- Cog categories.
- Then the tutorial.

**Built in:**
- Brave browser ✅ (installed as a Flatpak on first boot).
- Full media codecs ✅

**Updates:** a notification with a button. Nothing is forced.

**Rule:** nothing an average user needs may require the terminal.
