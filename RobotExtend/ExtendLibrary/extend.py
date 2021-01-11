# -*- coding:utf-8 -*-
'''
Created on 2021
@author zhu.liyuan

该扩展关键字在终端程序自动化项目（Robotframework+AutoItlibarary）中添加创建
'''

import os,time,sys
from robot.api import logger
import win32api
import win32con

class Extend(object):

    def B2Q(self,ustring):
        """
        半角字符转换为全角字符返回
        :param ustring: 任意数字
        :return: 全角字符
        """
        rstring =""
        for uchar in ustring:
            inside_code=ord(uchar)
            if inside_code ==32:
                inside_code=12288
            elif inside_code>=32 and inside_code <=126:
                inside_code+=65248

            rstring+=unichr(inside_code)
        return  rstring

    def keybd_event(self,VK_CODE):
        """
        通过键盘编码模拟键盘操作
        :param VK_CODE: 键盘编码（可百度）
        小键盘0：VK_NUMPAD1(96)
        :return:
        """
        VK_CODE=int(VK_CODE)
        win32api.keybd_event(VK_CODE,0,0,0)
        win32api.keybd_event(VK_CODE,0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(2)
