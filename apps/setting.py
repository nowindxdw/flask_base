# coding: utf-8
import os

from apps import app


# 加速模式
SPEED_MODE = [("1", "IPSec"), ("2", "L2TP"), ("3", "PPTP"), ("4", "OPENVPN"), ("5", "OPENCONNECT")]


CLIENT_TYPE_CHOICES = [('10', '客户端'), ('20', 'APP'),('30', '联机宝'), ('40', '官网')]


CLIENT_TYPE_DICT = {'10': 'PC客户端', '20': 'APP', '30': '联机宝'}
CLIENT_APP = 20
CLIENT_PC = 10
CLIENT_LJB = 30

APP_TYPE_CHOICES = [('android', 'Android'), ('ios', 'IOS')]




