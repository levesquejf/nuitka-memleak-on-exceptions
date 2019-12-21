#!/usr/bin/env bash

docker build -t nuitka-memleak-on-exception-native -f Dockerfile-native .
docker run nuitka-memleak-on-exception-native
