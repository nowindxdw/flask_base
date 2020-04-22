#!/usr/bin/env python
# -*- encoding:utf-8 -*-
#
# __author__ = 'QeeYou'
# __file__ = 'exceptions.py'
# __date__ = '2017/7/10 22:03'

class BaseException(Exception):
    """
    自定义异常类基类
    """
    def __init__(self, msg):
        self._msg = str(msg)

    def __str__(self):
        return repr(self._msg)

class MemcacheURIError(BaseException):
    """
    Memcached的地址类型异常
    """
    def __init__(self, msg):
        super(self.__class__, self).__init__(msg)

class PasswordReadError(BaseException):
    """
    web 密码不可读取异常
    """
    def __init__(self, msg):
        super(self.__class__, self).__init__(msg)