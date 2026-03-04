FROM debian:stable-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libtiff-dev libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /opt/bin/

COPY bin/x86_64-pc-linux-gnu/microstack26a_x86_64-pc-linux-gnu /opt/bin

RUN cd /opt/bin && ln -s microstack26a_x86_64-pc-linux-gnu microstack

ENTRYPOINT ["/opt/bin/microstack"]
