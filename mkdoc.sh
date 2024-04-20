#!/bin/bash

docker build  -t tibell/sentiment:1.0.0 .
docker run -it --rm -p 8090:8090  tibell/sentiment:1.0.0
