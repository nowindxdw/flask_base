# -*- coding: utf-8 -*-
import requests

temp_url = "http://api.sendcloud.net/apiv2/mail/sendtemplate"
direct_url = "http://api.sendcloud.net/apiv2/mail/send"
back_url = "http://api.sendcloud.net/apiv2/bounce/list"
API_USER = 'postmaster@postermaster.sendcloud.org'
API_KEY = 'uBLEPbG8UrjPUnUq'


def send_direct(to, s_from='postmaster@qeeyou.sendcloud.org',
                from_name='奇游加速器', subject='', content=''):
    """ 直接发送邮件 """
    params = {
        "apiUser": API_USER,  # 使用api_user和api_key进行验证
        "apiKey": API_KEY,
        "to": to,  # 收件人地址, 用正确邮件地址替代, 多个地址用';'分隔
        "from": s_from,  # 发信人, 用正确邮件地址替代
        "fromName": from_name,
        "subject": subject,
        "html": content
    }

    if len(to) > 1:
        params['userAddressList'] = 'true'

    r = requests.post(direct_url, data=params)
