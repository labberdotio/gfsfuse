
# 
# Copyright (c) 2019, 2020, 2021, John Grundback
# All rights reserved.
# 

import re

from gfs.common.log import GFSLogger
from gfs.common.base import GFSBase



class GremlinFSConfig(GFSBase):

    logger = GFSLogger.getLogger("GremlinFSConfig")

    @classmethod
    def defaults(clazz):
        return {
            # "mount_point": None,

            "gfs_host": None,
            "gfs_port": None,
            "gfs_username": None,
            # "gfs_password": None,
            "gfs_url": None,

            "log_level": GFSLogger.getLogLevel(),

        }

    def __init__(self, **kwargs):

        # Defaults
        self.setall(GremlinFSConfig.defaults())

        # Overrides
        self.setall(kwargs)

        # Build label regexes
        if self.has("labels"):
            for label_config in self.get("labels"):
                if "pattern" in label_config:
                    try:
                        label_config["compiled"] = re.compile(label_config["pattern"])
                    except Exception as e:
                        self.logger.exception(' GremlinFS: failed to compile pattern ' + label_config["pattern"], e)
                    pass
