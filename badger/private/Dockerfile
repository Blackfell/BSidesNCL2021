# challenge image build
FROM ubuntu:20.04

RUN apt-get update && apt-get install -yq --no-install-recommends socat libglib2.0-0 libpthread-stubs0-dev build-essential libc6-dev && rm -rf /var/lib/apt/lists/*

RUN /usr/sbin/useradd -m user

RUN mkdir /badger
COPY flag.txt /badger/
COPY entrypoint.sh /badger/
COPY badger /badger/

WORKDIR /badger
USER user
CMD ["/bin/bash", "./entrypoint.sh"]
