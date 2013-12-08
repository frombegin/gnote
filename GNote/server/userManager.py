#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.exceptions import UserAlreadyExistsError, UserIsLockedError, \
    UserNotExistsError, PasswordWrongError

from .services import DatabaseProvider, CacheProvider


class UserManager(object):
    
    def __init__(self, dbProvider, cacheProvider):
        
        super(UserManager, self).__init__()
        
        assert isinstance(dbProvider, DatabaseProvider)
        assert isinstance(cacheProvider, CacheProvider)
        
        self.__dbProvider = dbProvider
        self.__cacheProvider = cacheProvider
        
        
    def registerUser(self, user, password, userInfo):
 
        try:
            # 注册用户
            uid = self.__dbProvider.register(user, password)
            # 设置用户信息
            self.__dbProvider.setUserInfo(uid, userInfo)
            return True
        except UserAlreadyExistsError:
            return False    

    def _checkUserIsLocked(self, uid):
        if self.__dbProvider.isLocked(uid):
            raise UserIsLockedError()

    def loginUser(self, user, password):
        
        try:
            # 验证用户、密码
            uid = self.__dbProvider.checkPassword(user, password)
            
            # 检验用户是否被锁定
            self._checkUserIsLocked(uid)
            
            # 用户已经登录?
            if self.__cacheProvider.exists(uid):
                # TODO: 异地登录, 踢掉前面登录的
                userInfo = self.__dbProvider.getUserInfo(uid)
                self.__cacheProvider.set(uid, userInfo)
            return True, uid
        except UserNotExistsError:
            return False
        except PasswordWrongError:
            return False

    def getUserInfo(self, uid):
        userInfo = self.__cacheProvider.get(uid)
        if userInfo is None:
            userInfo = self.__dbProvider.getUserInfo(uid)
            if userInfo is not None:
                self.__cacheProvider.set(uid, userInfo)
        return userInfo
