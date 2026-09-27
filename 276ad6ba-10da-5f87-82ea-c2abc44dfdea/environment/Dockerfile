FROM debian:bookworm-slim@sha256:3783cc01769c7b2b1b83a5c5ad96c815348e28ed7da68e2e3687004faa906251 AS python-fetch
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates=20250419~deb12u1 curl=7.88.1-10+deb12u15 \
    && rm -rf /var/lib/apt/lists/*
ARG TARGETARCH
RUN case "${TARGETARCH}" in \
      amd64) ARCH=x86_64-unknown-linux-gnu ;; \
      arm64) ARCH=aarch64-unknown-linux-gnu ;; \
      *) echo "unsupported arch ${TARGETARCH}" && exit 1 ;; \
    esac \
    && mkdir -p /opt/python \
    && curl -fsSL "https://github.com/indygreg/python-build-standalone/releases/download/20240107/cpython-3.12.1+20240107-${ARCH}-install_only.tar.gz" | tar -xzC /opt/python --strip-components=1

FROM 426628337772.dkr.ecr.ap-south-1.amazonaws.com/argos/feldroy__air:pr-246@sha256:9c1dac5c9035de9e3336ce0438fcb38ab603d87fade50c892d6d61d765fbbd11
RUN if grep -qE "buster|bullseye" /etc/os-release 2>/dev/null; then \
        sed -i 's/deb.debian.org/archive.debian.org/g' /etc/apt/sources.list && \
        sed -i -E '/(buster|bullseye)[-\/](updates|security)/d' /etc/apt/sources.list && \
        echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99-eol-archive; \
    fi
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*
RUN rm -f /home/fix.patch /home/test.patch
RUN mkdir -p /workspace && ln -sfn /home/air /workspace/air \
    && git config --global --add safe.directory /home/air \
    && git config --global --add safe.directory /workspace/air
WORKDIR /workspace/air
ENV PYTHONUNBUFFERED=1
COPY --from=python-fetch /opt/python /opt/python
RUN /opt/python/bin/python3 -m venv /opt/openhands-sdk-venv \
    && /opt/openhands-sdk-venv/bin/pip install --no-cache-dir openhands-sdk==1.49.3 openhands-tools==1.49.3 fastapi==0.141.1
RUN [ -f /opt/openhands-sdk-venv/bin/python ] \
    && /opt/openhands-sdk-venv/bin/python -c "import openhands.sdk" \
    && command -v git >/dev/null && command -v curl >/dev/null && command -v stdbuf >/dev/null
