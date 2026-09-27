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

FROM 426628337772.dkr.ecr.ap-south-1.amazonaws.com/argos/gitoxidelabs__gitoxide:pr-2191@sha256:c8fa6b92d9fa4d897227cf494501ea30ad1c2230854c968bffca313075885cc3
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*
RUN rm -f /home/fix.patch /home/test.patch
RUN mkdir -p /workspace && ln -sfn /home/gitoxide /workspace/gitoxide \
    && git config --global --add safe.directory /home/gitoxide \
    && git config --global --add safe.directory /workspace/gitoxide
WORKDIR /workspace/gitoxide
ENV PYTHONUNBUFFERED=1
COPY --from=python-fetch /opt/python /opt/python
RUN /opt/python/bin/python3 -m venv /opt/openhands-sdk-venv \
    && /opt/openhands-sdk-venv/bin/pip install --no-cache-dir openhands-sdk==1.49.3 openhands-tools==1.49.3 fastapi==0.141.1
RUN [ -f /opt/openhands-sdk-venv/bin/python ] \
    && /opt/openhands-sdk-venv/bin/python -c "import openhands.sdk" \
    && command -v git >/dev/null && command -v curl >/dev/null && command -v stdbuf >/dev/null
