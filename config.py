#!/usr/bin/env python
# encoding: utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))
BASEDIR = basedir
DEBUG = False
SECRET_KEY = 'This is a secret key forexample'

# not end with else throw  AttributeError: 'tuple' object has no attribute 'drivername'
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:rootpassword@127.0.0.1/test?charset=utf8" # base管理

SQLALCHEMY_BINDS = {
    'base': "mysql+pymysql://root:rootpassword@127.0.0.1/test?charset=utf8",  # web数据库
    'website': "mysql+pymysql://root:rootpassword@127.0.0.1/website?charset=utf8",  # web数据库
    'otherdb': "mysql+pymysql://root:rootpassword@127.0.0.1/otherdb?charset=utf8",  # other管理
}
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_COMMIT_ON_TEARDOWN = False
SQLALCHEMY_AUTOFLUSH = False
SQLALCHEMY_ECHO = True

REDIS_URL = 'redis://:@127.0.0.1:6379'

