#!/usr/bin/env python
# -*- encoding:utf-8 -*-
#
# __author__ = 'QeeYou'
# __file__ = 'log.py'
# __date__ = '2017/7/9 20:20'

import os
import logging
import logging.handlers

def init_log(log_path, level=logging.INFO, when="D", backup=7,
        format="%(levelname)s: %(asctime)s: %(filename)s:%(lineno)d * %(thread)d %(message)s",
        datefmt="%m-%d %H:%M:%S"):
    """
    init_log - initialize logs module

    Args:
        log_path        - Log file path prefix.
                          Log data will go to two files: log_path.logs and log_path.logs.wf
                          Any non-exist parent directories will be created automatically
        level           - msg above the level will be displayed
                          DEBUG < INFO < WARNING < ERROR < CRITICAL
                          the default valeue is logging.INFO
        when            - how to split the logs file by time interval
                          'S' : Seconds
                          'M' : Minutes
                          'H' : Hours
                          'D' : Days
                          'W' : Week day
                          default value: 'D'
        format          - format of the logs
                          default format:
                          %(levelname)s: %(asctime)s: %(filename)s:%(lineno)d * %(thread)d \
                                  %(message)s
                          eg:
                            INFO: 12-09 18:02:42: logs.py:40 * 18511695029 HELLO WORLD
        backup          - how mandy bakcup file to keep
                          default value: 7

    Rais:
        OSError: fail to create logs directories
        IOError: fail to open logs file
    """
    formatter = logging.Formatter(format, datefmt)
    logger = logging.getLogger()
    logger.setLevel(level)

    dir = os.path.dirname(log_path)
    if not os.path.isdir(dir):
        os.makedirs(dir)

    handler = logging.handlers.TimedRotatingFileHandler(log_path,
                                                        when=when,
                                                        backupCount=backup)
    handler.setLevel(level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    handler = logging.handlers.TimedRotatingFileHandler(log_path + ".wf",
                                                        when=when,
                                                        backupCount=backup)
    handler.setLevel(logging.WARNING)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
