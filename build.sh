#!/bin/bash
set -e

LOCAL_REGISTRY="${LOCAL_REGISTRY:-buildregistry.localdomain}"

GIT_BRNCH=$(git rev-parse --abbrev-ref HEAD)
GIT_SHA=$(git rev-parse HEAD | cut -c 1-8)

image() {
    BASE="$1"
    IMAGE="${LOCAL_REGISTRY}/gfs-fuse:${BASE}-${GIT_BRNCH}-${GIT_SHA}"
    LATEST_IMAGE="${LOCAL_REGISTRY}/gfs-fuse:${BASE}-latest"
    docker build -t $IMAGE -f docker/Dockerfile.$BASE .
    docker push $IMAGE
    docker tag $IMAGE $LATEST_IMAGE
    docker push $LATEST_IMAGE
}

image "alpine"
image "debian"
image "theia"

LATEST_THEIA_IMAGE="${LOCAL_REGISTRY}/gfs-fuse:theia-latest"
LATEST_IMAGE="${LOCAL_REGISTRY}/gfs-fuse:latest"
docker tag $LATEST_THEIA_IMAGE $LATEST_IMAGE
