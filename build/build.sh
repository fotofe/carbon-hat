#!/usr/bin/bash
# Runs inside the image build (see Containerfile).
set -euxo pipefail

# Our own files: textures, wallpapers, themes, tuning, services.
cp -a /ctx/system_files/. /

# Packages. Brave replaces Firefox; it is installed as a Flatpak on first
# boot (carbonhat-flatpaks.service) because the Brave RPM writes to /opt,
# which is not part of an Atomic image.
if rpm -q firefox; then
    dnf5 -y remove firefox firefox-langpacks
fi
command -v kwriteconfig6 || dnf5 -y install /usr/bin/kwriteconfig6

# Name and version.
sed -i \
    -e 's/^NAME=.*/NAME="Carbon hat"/' \
    -e "s/^PRETTY_NAME=.*/PRETTY_NAME=\"Carbon hat ${VERSION} (Fedora 44 base)\"/" \
    -e 's/^VARIANT=.*/VARIANT="Carbon hat"/' \
    -e 's/^VARIANT_ID=.*/VARIANT_ID=carbonhat/' \
    -e '/^IMAGE_ID=/d' -e '/^IMAGE_VERSION=/d' \
    /usr/lib/os-release
printf 'IMAGE_ID=carbon-hat\nIMAGE_VERSION=%s\n' "$VERSION" >> /usr/lib/os-release
echo "$VERSION" > /usr/share/carbonhat/version
kwriteconfig6 --file /etc/xdg/kcm-about-distrorc --group General --key Variant "${VERSION} (Fedora 44 base)"

# Default look for new users. Fedora also keeps KDE defaults in its
# kde-settings profile, so set both places.
for f in /etc/xdg/kdeglobals /usr/share/kde-settings/kde-profile/default/xdg/kdeglobals; do
    if [ "$f" = /etc/xdg/kdeglobals ] || [ -e "$f" ]; then
        kwriteconfig6 --file "$f" --group KDE --key LookAndFeelPackage org.carbonhat.dark
        kwriteconfig6 --file "$f" --group General --key ColorScheme CarbonHatDark
    fi
done

chmod +x /usr/libexec/carbonhat/*
systemctl enable carbonhat-memory.service carbonhat-flatpaks.service
