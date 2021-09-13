#!/usr/bin/env bash
EXPOSE_PORT=1337

sudo docker kill badger
sudo docker rm badger
sudo docker build -t badger .
sudo docker run -d --name badger -p $EXPOSE_PORT:1337 badger
