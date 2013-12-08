#!/usr/bin/env python
# -*- coding: utf-8 -*-

class GnoteException(Exception):
    pass

class UserAlreadyExistsError(GnoteException):
    pass

class UserNotExistsError(GnoteException):
    pass

class PasswordWrongError(GnoteException):
    pass

class UserIsLockedError(GnoteException):
    pass