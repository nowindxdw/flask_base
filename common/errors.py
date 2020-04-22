#!/usr/bin/env python
# encoding: utf-8

class BaseError(Exception):
    """
    所有自定义异常类的基类
    """
    def __init__(self, msg):
        self._msg = str(msg)

    def __str__(self):
        return repr(self._msg)

class HostConfigError(BaseError):
    """
    主机区配置异常类
    """
    def __init__(self, msg):
        super(self.__class__, self).__init__(msg)