#!/usr/bin/env python
# -*- coding: utf-8 -*-

class DatabaseProvider(object):
    '''数据库接口'''
    
    def __init__(self):
        pass
    
    def registerUser(self, user, password):
        pass
    
    def removeUser(self, user):  # only admin
        pass
    
    def lockUser(self, user):  # only admin
        pass
    
    def unlockUser(self, user):  # only admin
        pass

    def isUserLocked(self, userId):
        pass
    
    def changePassword(self, user, password):
        pass
    
    def getUserInfo(self, user):
        pass

    def setUserInfo(self, user, userInfo):
        pass
    
    def checkPassword(self, user, password):
        pass
 

class CacheProvider(object):
    # 缓存
    
    def get(self, key):
        pass
    
    def set(self, key, value):
        pass
    
    def exists(self, key):
        pass
    
    def delete(self, key):
        pass
