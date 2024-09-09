
# 
# Copyright (c) 2019, 2020, 2021, John Grundback
# All rights reserved.
# 

from gfs.common.log import GFSLogger
from gfs.common.base import GFSBase

from gfs.gfs import GremlinFS
from gfs.lib.util import GremlinFSUtils
from gfs.lib.event import GremlinFSEvent



class GFSNode(GFSBase):

    logger = GFSLogger.getLogger("GFSNode")

    @classmethod
    def parse(clazz, id):
        return None

    @classmethod
    def infer(clazz, field, obj, default = None):
        parts = clazz.parse( obj )
        if not field in parts:
            return default
        return parts.get(field, default)

    @classmethod
    def label(clazz, name, label, fstype = "file", default = None):
        return label

    @classmethod
    def vals(clazz, invals):
        if not invals:
            return {}

        vals = {}
        vals["id"] = GremlinFSUtils.value( invals.get("id") )
        vals["label"] = GremlinFSUtils.value( invals.get("label") )
        for key, val in invals.get("properties").items():
            vals[key] = GremlinFSUtils.value( val )

        return vals

    @classmethod
    def fromMap(clazz, map):
        vals = clazz.vals(map.get("@value"))
        return clazz(**vals)

    @classmethod
    def fromMaps(clazz, maps):
        nodes = []
        for map in maps:
            vals = clazz.vals(map.get("@value"))
            nodes.append(clazz(**vals))
        return nodes

    @classmethod
    def fromVal(clazz, val = [], names = []):
        vals = clazz.vals(map)
        return clazz(**vals)

    @classmethod
    def fromVals(clazz, vals = [], names = []):
        nodes = []
        for val in vals:
            vals = {}
            for i, name in enumerate(names):
                vals[name] = val[i]
            nodes.append(clazz(**vals))
        return nodes

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.set(key, value)

    # 

    def api(self):
        return GremlinFS.operations().api()

    def query(self, query, node = None, default = None):
        return self.utils().query(query, node, default)

    def eval(self, command, node = None, default = None):
        return self.utils().eval(command, node, default)

    def config(self, key = None, default = None):
        return GremlinFS.operations().config(key, default)

    def utils(self):
        return GremlinFS.operations().utils()

    def labelConfig(self):
        node = self
        config = None

        for label_config in GremlinFS.operations().config("labels", []):
            if "label" in label_config and label_config["label"] == node.get('label', None):
                config = label_config

        return config

    # 

    def toid(self, short = False):
        pass

    def matches(self, inmap):
        pass

    def hasProperty(self, name, prefix = None):
        pass

    def getProperty(self, name, default = None, encoding = None, prefix = None):
        pass

    def setProperty(self, name, data = None, encoding = None, prefix = None):
        pass

    def unsetProperty(self, name, prefix = None):
        pass

    def setProperties(self, properties, prefix = None):
        pass

    def getProperties(self, prefix = None):
        pass

    def readProperty(self, name, default = None, encoding = None, prefix = None):
        return self.getProperty(name, default, encoding = encoding, prefix = prefix)

    def writeProperty(self, name, data, encoding = None, prefix = None):
        return self.setProperty(name, data, encoding = encoding, prefix = prefix)

    def invoke(self, script, handler, context = {}):
        pass

    def handlers(self):
        pass

    def handler(self, event):
        pass

    def event(self, event, chain = [], data = {}, propagate = True):
        pass
