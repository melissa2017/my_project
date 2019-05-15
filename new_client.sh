#!/bin/bash

if [ "$#" -ne 2 ] || [ "$1" = "--help" ]; then
  echo "Usage: $0 client_name service_url" >&2
  echo "Service URL: http://0.0.0.0:5000" >&2
  exit 1
fi


docker build -t "$1" client/
docker run --net=host -ti "$1" "$2"