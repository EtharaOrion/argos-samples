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
COPY --from=python-fetch /opt/python /opt/python
RUN /opt/python/bin/python3 -m pip install --no-cache-dir "multi-swe-bench @ git+https://github.com/Ethara-Ai/multi-swe-bench.git@447ddbd639e4ec60376282ccee32ad1ab60afb69"
RUN rm -f /home/fix.patch /home/test.patch
COPY . /tests/
