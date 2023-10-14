#!/bin/sh

# 
docker run \
	-e GFSAPI_HOST='gfs.labber.io' \
	-e GFSAPI_PORT='80' \
	--add-host gfs.labber.io:10.88.88.191 \
	--rm -it \
	--privileged --device /dev/fuse --cap-add SYS_ADMIN \
	--entrypoint bash buildregistry.localdomain/gfs-fuse:debian-latest

