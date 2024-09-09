
# 
# Copyright (c) 2019, 2020, 2021, John Grundback
# All rights reserved.
# 

from gfs.common.log import GFSLogger
from gfs.common.base import GFSBase

from gfs.error.error import GFSError
from gfs.error.error import GFSExistsError
from gfs.error.error import GFSNotExistsError
from gfs.error.error import GFSIsFileError
from gfs.error.error import GFSIsFolderError

from gfs.gfs import GremlinFS
from gfs.lib.util import GremlinFSUtils



class GremlinFSPath(GFSBase):

    logger = GFSLogger.getLogger("GremlinFSPath")

    @classmethod
    def paths(clazz):
        return {
        }

    @classmethod
    def path(clazz, path):
        paths = GremlinFSPath.paths()
        if paths and path in paths:
            return paths[path]
        return None

    @classmethod
    def expand(clazz, path):
        return GremlinFS.operations().utils().splitpath(path)

    @classmethod
    def atpath(clazz, path, node = None):
        return None

    @classmethod
    def pathnode(clazz, nodeid, parent, path):

        node = None
        return node

    @classmethod
    def pathparent(clazz, path = []):

        root = None
        parent = root
        return parent

    @classmethod
    def match(clazz, path):

        match = {
        }

        return GremlinFSPath(
        )

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

    # 

    def enter(self, functioname, *args, **kwargs):
        self.logger.debug(' GremlinFSPath: ENTER: %s ' % (functioname))
        self.logger.debug(args)
        self.logger.debug(kwargs)

    # 

    def root(self):
        root = None
        return root

    def node(self):
        return self._node

    def parent(self):
        return self._parent

    # 

    def isFolder(self):
        default = False
        return default

    def isFile(self):
        default = False
        return default

    def isLink(self):
        default = False
        return default

    def isFound(self):
        default = False
        return default


    # 
    # Folder CRUD
    # 
    # - createFolder
    # - readFolder
    # - renameFolder
    # - deleteFolder
    # 


    def createFolder(self):
        default = None
        return default

    def readFolder(self):
        entries = []
        return entries

    def renameFolder(self, newmatch):
        pass

    def deleteFolder(self):
        pass


    # 
    # File CRUD
    # 
    # - createFile
    # - readFile
    # - writeFile
    # - renameFile
    # - deleteFile
    # 


    def createFile(self, data = None):
        default = data
        return default

    def readFile(self, size = 0, offset = 0):
        return None

    def readFileLength(self):
        return 0

    def writeFile(self, data, offset = 0):
        pass

    def clearFile(self):
        pass

    def renameFile(self, newmatch):
        pass

    def deleteFile(self):
        pass


    # 
    # Link CRUD
    # 
    # - createLink
    # - readLink
    # - renameLink
    # - deleteLink
    # 


    def createLink(self, sourcematch):
        default = None
        return default        

    def readLink(self):
        default = None
        return default

    def deleteLink(self):
        default = None
        return default

    # 

    def readNode(self, size = 0, offset = 0):
        default = None
        return default

    def writeNode(self, data, offset = 0):
        default = data
        return default

    def clearNode(self):
        default = None
        return default

    def moveNode(self, newmatch):
        default = None
        return default

    def deleteNode(self):
        default = None
        return default

    def setProperty(self, key, value):
        return True

    def getProperty(self, key, default = None):
        return default
