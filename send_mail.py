#!/usr/bin/env python
# coding:utf-8
"""
Name : send_mail.py
Author  : anne
Time    : 2019-10-02 15:51
Desc:
"""
import os
from django.core.mail import send_mail
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
# if __name__ == '__main__':
#     send_mail(
#         '来自姜凡的测试邮件',
#         '测试请勿回复',
#         'jiangfanm95@126.com',
#         ['1760103967@qq.com'],
#     )