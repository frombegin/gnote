#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os


    




def selftest():
    ui = UserInfo()
    ui.name = u"张三"
    ui.email = u"zhang.san@gmail.com"
    assert unicode(ui) == u"张三 <zhang.san@gmail.com>"
    print unicode(ui)

if __name__ == "__main__":
    selftest()
