#!/usr/bin/env bash

docker build -t nuitka-memleak-on-exception-nuitka -f Dockerfile-nuitka .
docker run nuitka-memleak-on-exception-nuitka
