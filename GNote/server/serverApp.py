#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .userManager import UserManager

from .services import CacheProvider, DatabaseProvider

class ServerApp(object):
    
    def __init__(self):
        super(ServerApp, self).__init__()
        self.__dbPovider = None
        self.__cacheProvider = None
        self.__userManager = None
        self.__isRunning = False

    def getDbPovider(self): 
        return self.__dbPovider

    def getCache(self): 
        return self.__cacheProvider

    def getUserManager(self): 
        return self.__userManager

    def getIsRunning(self):
        return self.__isRunning

    def start(self):
        if self.__isRunning: return
        
        self.__dbPovider = None  # TODO: create Database Provider
        self.__cacheProvider = None  # TODO: create CacheProvider
        self.__userManager = UserManager(self.__dbPovider, self.__cacheProvider)
        
    def stop(self):
        if not self.__isRunning: return
        
        self.__userManager = None
        self.__cacheProvider = None
        self.__dbPovider = None

    dbPovider = property(getDbPovider, None, None, None)
    cache = property(getCache, None, None, None)
    userManager = property(getUserManager, None, None, None)
    isRunning = property(getIsRunning, None, None, None)
