#!/bin/sh

LOCAL_REGISTRY="${LOCAL_REGISTRY:-buildregistry.localdomain}"

GIT_BRNCH=$(git rev-parse --abbrev-ref HEAD)
GIT_SHA=$(git rev-parse HEAD | cut -c 1-8)

BASE="debian"
CONTAINER_NAME="gfsfuse"
LATEST_IMAGE="${LOCAL_REGISTRY}/gfs-fuse:${BASE}-latest"

# 
docker exec -it ${CONTAINER_NAME} /bin/bash
