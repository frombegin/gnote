#!/usr/bin/env python
# -*- coding: utf-8 -*-
 

MALE, FEMALE = (0, 1)

class UserInfo(object):

    def __init__(self):
        super(UserInfo, self).__init__()
        self.__id = -1
        self.__name = u""
        self.__sex = MALE
        self.__email = u""
        self.__registered = False
        
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getSex(self):
        return self.__sex

    def getEmail(self):
        return self.__email

    def getRegistered(self):
        return self.__registered


    def setId(self, value):
        self.__id = value

    def setName(self, value):
        self.__name = value

    def setSex(self, value):
        self.__sex = value

    def setEmail(self, value):
        self.__email = value

    def setRegistered(self, value):
        self.__registered = value

    def __unicode__(self):
        return u"%s <%s>" % (self.__name, self.__email)

    id = property(getId, setId, None, None)
    name = property(getName, setName, None, None)
    sex = property(getSex, setSex, None, None)
    email = property(getEmail, setEmail, None, None)
    registered = property(getRegistered, setRegistered, None, None)
    

# -----------------------------------------------------------------------------

class MemberInfo(object):
    
    def __init__(self):
        super(MemberInfo, self).__init__()
        self.__uid = -1
        self.__name = u""
        self.__isAdmin = False
        
    def __unicode__(self):
        return u"{%s}" % self.__name if self.__isAdmin else self.__name

# -----------------------------------------------------------------------------

class GroupInfo(object):
    
    def __init__(self):
        super(GroupInfo, self).__init__()
        self.__name = u""
        self.__description = u""
        self.__tags = u""
        self.__members = []
        self.__creatorId = -1
        
    def __unicode__(self):
        return u"%s (%s)" % (self.__name, self.__description)
    
# -----------------------------------------------------------------------------

class Book(object):
    
    def __init__(self):
        super(Book, self).__init__()

# -----------------------------------------------------------------------------

class Note(object):
    
    def __init__(self):
        super(Note, self).__init__()

# -----------------------------------------------------------------------------

class Tag(object):
    
    def __init__(self):
        super(Tag, self).__init__()
        self.__tag = u""
        self.__popular = 0
        
# -----------------------------------------------------------------------------

class TagCloud(object):
    
    def __init__(self):
        super(TagCloud, self).__init__()
        self.__tags = []
        
    def sortByPopular(self):
        pass
    
    def sortByLetter(self):
        pass
    
# -----------------------------------------------------------------------------

