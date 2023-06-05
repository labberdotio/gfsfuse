
# 
# Copyright (c) 2020, 2021, John Grundback
# All rights reserved.
# 

import requests

import simplejson as json

import contextlib
import addict
from addict import Dict

from gfs.common.log import GFSLogger



class GFSAPIError(Exception):

    def __init__(self, error):
        pass



class GFSAPI():

    logger = GFSLogger.getLogger("GFSAPI")

    def __init__(
        self,

        gfs_host,
        gfs_port,
        gfs_username,
        gfs_password,

        **kwargs):

        self.gfs_host = gfs_host
        self.gfs_port = gfs_port
        self.gfs_username = gfs_username
        self.gfs_password = gfs_password

        self.api_version = "api/v1.0"
        self.api_namespace = "gfs1"

    def decode(self, data):

        if data:

            try:

                # convert to string
                data = data.decode(
                    encoding='utf-8', 
                    errors='strict'
                )

                return data

            except:
                return data

        return data

    def json(self, data):

        if not data:
            return None

        return json.loads(data)

    def apiid(self, resourceid):
        pass

    def apiurl(self, resource, properties = {}):
        pass

    def apiget(self, resource, properties = {}):
        pass

    def apipost(self, resource, data = {}):
        pass

    def apiput(self, resource, data = {}):
        pass

    def apidelete(self, resource):
        pass

    #
    #
    #

    def query(self, resource, match = {}, fields = []):
        pass

    def get(self, resource, resourceid, property = None, fields = []):
        pass

    def create(self, resource, data = {}, fields = []):
        pass

    def update(self, resource, resourceid, data = {}, fields = []):
        pass

    def delete(self, resource, resourceid):
        pass

    def set(self, resource, resourceid, property, value):
        pass

    def unset(self, resource, resourceid, property):
        pass

    #
    #
    #



class GFSCachingAPI(GFSAPI):

    logger = GFSLogger.getLogger("GFSCachingAPI")

    def __init__(
        self,

        gfs_host,
        gfs_port,
        gfs_username,
        gfs_password,

        **kwargs):

        super().__init__(

            gfs_host,
            gfs_port,
            gfs_username,
            gfs_password,

            **kwargs
        )

        self.caching = True # False
        self.cache = Dict() # {}

    # 

    def lookupCache(self, path, oper):

        from datetime import datetime
        self.logger.debug("CACHE: lookup: path: %s, oper: %s", path, oper)

        pick = False
        cachehit = self.cache[path][oper]
        if cachehit:
            if cachehit['expire']:
                if cachehit['expire'] > datetime.now():
                    self.logger.debug("CACHE: lookup: cachehit: found entry with expire, not expired")
                    pick = cachehit
                else:
                    self.logger.debug("CACHE: lookup: cachehit: found entry with expire, is expired")
            else:
                pick = cachehit

        if pick:
            cachehit = pick
            exp = ""
            if cachehit['expire']:
                exp = str(cachehit['expire'])
            self.logger.debug("CACHE: lookup: cachehit: PATH: %s, OPER: %s, CREATED: %s, EXPIRE: %s", 
                cachehit.path, cachehit.oper, str(cachehit.created), exp
            )
            return cachehit.data

        else:
            return False

    def prepareCache(self, path, oper, expire_seconds = None):

        from datetime import datetime, timedelta
        self.logger.debug("CACHE: prepare: path: %s, oper: %s", path, oper)

        expire = None
        if expire_seconds:
            time = datetime.now()
            expire = time + timedelta(0, expire_seconds) # days, seconds, then other fields.

        self.cache[path][oper]['path'] = path
        self.cache[path][oper]['oper'] = oper
        self.cache[path][oper]['flags'] = 1 # Indicate not yet active cache entry
        if expire:
            self.cache[path][oper]['expire'] = expire

        return self.cache[path][oper]

    def finalizeCache(self, path, oper, data):

        self.logger.debug("CACHE: finalize: path: %s, oper: %s", path, oper)
        self.cache[path][oper]['data'] = data
        self.cache[path][oper]['flags'] = 0 # Indicate active cache entry

        return self.cache[path][oper]

    def readCache(self, path, oper):

        cachepath = path
        cacheoper = oper
        expire = 60

        if cachepath and self.caching:
            try:
                cachedata = self.lookupCache(cachepath, cacheoper)
                if cachedata:
                    return cachedata
            except Exception as e:
                self.logger.warning("Client call not fatal error: lookup cache error: exception: %s" % ( str(e) ))
                self.logger.warning(e)

        if cachepath and self.caching:
            cache = None
            try:
                cache = self.prepareCache(cachepath, cacheoper, expire)
            except Exception as e:
                self.logger.warning("Client call not fatal error: prepare cache error: exception: %s" % ( str(e) ))
                self.logger.warning(e)

    def updateCache(self, path, oper, data):

        cachepath = path
        cacheoper = oper

        if data:
            if cachepath and self.caching:
                try:
                    self.finalizeCache(cachepath, cacheoper, data)
                except Exception as e:
                    self.logger.warning("Client call not fatal error: finalize cache error: exception: %s" % ( str(e) ))
                    self.logger.warning(e)

        return data

    def clearCache(self, path = None):

        cachepath = path

        if cachepath:
            self.logger.debug("CACHE: clear: path: %s", cachepath)
            del self.cache[path]

        else:
            self.logger.debug("CACHE: clear full")
            self.cache = Dict() # {}

    # 

    def apiget(self, resource, properties = {}):

        url = self.apiurl(
            resource, 
            properties
        )

        cachepath = url
        cacheoper = 'GET'

        # resp = None
        data = None

        cachedata = self.readCache(cachepath, cacheoper)
        if cachedata:
            # resp = cachedata
            data = cachedata

        else:
            resp = requests.get(
                url
            )
            data = {
                "status": resp.status_code,
                "data": self.decode(resp.text)
            }
            self.updateCache(cachepath, cacheoper, data)

        # if resp.status_code != 200:
        if data.get("status", 0) != 200:
            raise GFSAPIError(
                '{} {} {}'.format(
                    "GET",
                    url,
                    data.get("status", 0)
                )
            )

        return data.get("data", None)

    def apipost(self, resource, data = {}):
        ret = super().apipost(resource, data)
        # Clear full cache for now
        self.clearCache()
        return ret

    def apiput(self, resource, data = {}):
        ret = super().apiput(resource, data)
        # Clear full cache for now
        self.clearCache()
        return ret

    def apidelete(self, resource):
        ret = super().apidelete(resource)
        # Clear full cache for now
        self.clearCache()
        return ret
