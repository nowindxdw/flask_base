# -*- coding: utf-8 -*-
import decimal
import datetime
import time
import json

import sqlalchemy
from sqlalchemy.ext.declarative import DeclarativeMeta
from redis import StrictRedis

from apps import app
from apps.setting import CLIENT_TYPE_CHOICES


def tuple_value_to_list(tuple_value):
    if not tuple_value:
        return []

    ret = []
    for y in tuple_value:
        if isinstance(y, decimal.Decimal):
            ret.append(float(y))
        elif isinstance(y, datetime.datetime):
            ret.append(time.mktime(y.timetuple()))
        elif isinstance(y, sqlalchemy.sql.functions.now):
            ret.append(int(time.time()))
        elif y is None:
            ret.append('')
        else:
            ret.append(y)
    return ret


def get_clients_dict():
    """ 获取终端类型字典 """
    ret = {x[0]: x[1] for x in CLIENT_TYPE_CHOICES}
    return ret


def redis_scan_keys(redis_server, match_key):
    """ 用scan遍历redis,获取匹配到的key """
    index, total_keys = redis_server.scan(cursor=0, match=match_key, count=1000)
    while index != 0:
        index, keys = redis_server.scan(cursor=index, match=match_key, count=1000)
        total_keys.extend(keys)
    return total_keys


def get_node_redis_conn():
    """
    获取node节点分配系统redis连接
    :return:
    """
    mc = StrictRedis.from_url(app.config['REDIS_URL'],
                              socket_connect_timeout=1, socket_timeout=6)
    return mc


class serializable_them(json.JSONEncoder):
    """
    有些类型是不能序列化的. 我现在要让他们能序列化.

    """
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, decimal.Decimal):
            return str(obj)
        elif isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj)
                          if not x.startswith('_')
                          and x != 'metadata'
                          and x != 'member_id']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # 试试能不能序列化
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


