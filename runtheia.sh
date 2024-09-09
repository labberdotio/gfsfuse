#!/bin/sh

LOCAL_REGISTRY="${LOCAL_REGISTRY:-buildregistry.localdomain}"

GIT_BRNCH=$(git rev-parse --abbrev-ref HEAD)
GIT_SHA=$(git rev-parse HEAD | cut -c 1-8)

BASE="theia"
CONTAINER_NAME="gfsfusetheia"

# buildregistry.localdomain/gfs-fuse  theia-latest          1dac1671f856  3 minutes ago  745MB  # 1.25
# buildregistry.localdomain/gfs-fuse  theia-theia-a2a8e475  1dac1671f856  3 minutes ago  745MB  # 1.25
# buildregistry.localdomain/gfs-fuse  theia-theia-5f72383f  d3ac09f93ad6  13 hours ago   695MB  # 1.18
# buildregistry.localdomain/gfs-fuse  theia-theia-f0b923dd  af2f0bd1591c  14 hours ago   782MB  # 1.7
LATEST_IMAGE="${LOCAL_REGISTRY}/gfs-fuse:${BASE}-latest" # 1.25
# LATEST_IMAGE="${LOCAL_REGISTRY}/gfs-fuse:${BASE}-theia-a2a8e475" # 1.25
# LATEST_IMAGE="${LOCAL_REGISTRY}/gfs-fuse:${BASE}-theia-5f72383f" # 1.18
# LATEST_IMAGE="${LOCAL_REGISTRY}/gfs-fuse:${BASE}-theia-f0b923dd" # 1.7.0

# 
# docker run \
# 	-e GFSAPI_HOST='gfs.labber.io' \
# 	-e GFSAPI_PORT='80' \
# 	--add-host gfs.labber.io:10.88.88.191 \
# 	--rm -it \
# 	--privileged --device /dev/fuse --cap-add SYS_ADMIN \
# 	--name ${CONTAINER_NAME} \
# 	--entrypoint bash ${LATEST_IMAGE}

docker kill ${CONTAINER_NAME} || true
docker rm ${CONTAINER_NAME} || true

docker run \
	-e GFSAPI_HOST='gfs.labber.io' \
	-e GFSAPI_PORT='80' \
	--add-host gfs.labber.io:10.88.88.191 \
	--rm \
	--privileged --device /dev/fuse --cap-add SYS_ADMIN \
	--name ${CONTAINER_NAME} \
	-p 0.0.0.0:3000:3000/tcp --expose 3000 ${LATEST_IMAGE}
