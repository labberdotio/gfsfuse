#!/bin/sh

LOCAL_REGISTRY="${LOCAL_REGISTRY:-buildregistry.localdomain}"

GIT_BRNCH=$(git rev-parse --abbrev-ref HEAD)
GIT_SHA=$(git rev-parse HEAD | cut -c 1-8)

BASE="debian"
CONTAINER_NAME="gfsfuse"
LATEST_IMAGE="${LOCAL_REGISTRY}/gfs-fuse:${BASE}-latest"

# 
docker run \
	-e GFSAPI_HOST='gfs.labber.io' \
	-e GFSAPI_PORT='80' \
	--add-host gfs.labber.io:10.88.88.191 \
	--rm -it \
	--privileged --device /dev/fuse --cap-add SYS_ADMIN \
	--name ${CONTAINER_NAME} \
	--entrypoint bash ${LATEST_IMAGE}
