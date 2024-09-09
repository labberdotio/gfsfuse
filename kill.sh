#!/bin/sh

LOCAL_REGISTRY="${LOCAL_REGISTRY:-buildregistry.localdomain}"

GIT_BRNCH=$(git rev-parse --abbrev-ref HEAD)
GIT_SHA=$(git rev-parse HEAD | cut -c 1-8)

BASE="alpine"
CONTAINER_NAME="gfsfuse"
LATEST_IMAGE="${LOCAL_REGISTRY}/gfs-fuse:${BASE}-latest"

docker kill ${CONTAINER_NAME} || true
docker rm ${CONTAINER_NAME} || true
