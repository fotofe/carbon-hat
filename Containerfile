# Carbon hat system image. GitHub builds this (see .github/workflows/build.yml).
#
# Base: Universal Blue's Fedora 44 KDE Atomic image. It is Fedora Kinoite
# plus the full media codecs and hardware video drivers.
ARG FEDORA=44

FROM scratch AS ctx
COPY build /build
COPY system_files /system_files

FROM ghcr.io/ublue-os/kinoite-main:${FEDORA}
ARG VERSION=0.0.0
RUN --mount=type=bind,from=ctx,source=/,target=/ctx \
    --mount=type=cache,dst=/var/cache \
    --mount=type=cache,dst=/var/log \
    --mount=type=tmpfs,dst=/tmp \
    VERSION="$VERSION" /ctx/build/build.sh
RUN ["bootc", "container", "lint"]
