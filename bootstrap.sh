#!/usr/bin/env bash

CONTAINER_IP=$(cat /etc/hosts | grep 172 | cut -f 1 -d$'\t')
echo "Found IP of container: $CONTAINER_IP"

GFS_MOUNTPOINT="/gfs"
# mkdir -p $GFS_MOUNTPOINT

# GFSAPI_HOST=${GFSAPI_HOST:-10.88.88.183}
# GFSAPI_USER=${GFSAPI_USER:-...}
# GFSAPI_PASSWORD=${GFSAPI_PASSWORD:-...}
GFSAPI_HOST=${GFSAPI_HOST:-gfs-api}
GFSAPI_PORT=${GFSAPI_PORT:-5000}

sudo chmod a+rwx /dev/fuse

sudo python3 \
    /gfsfuse/src/py/main.py \
    $GFS_MOUNTPOINT \
    $GFSAPI_HOST \
    $GFSAPI_PORT
