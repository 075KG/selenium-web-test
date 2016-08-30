# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import time

def test_clientid_psw(path):
    """
    打开网页，把从文件读出来的信息逐条输入到测试窗口
    """
    #wd = webdriver.Chrome()
    #wd.get("http://renren.com/")#这里是要测试的网址

    content_seq = get_id_psw_from_file(path)
    #玩野驱动函数看这里http://selenium-python.readthedocs.io/locating-elements.html
    for content in content_seq:
        wd = webdriver.Chrome()
        wd.get("http://renren.com/")#这里是要测试的网址
        wd.find_element_by_id("email").clear()                 
        wd.find_element_by_id("email").send_keys(content[0])  #输入帐号
        wd.find_element_by_id("password").send_keys(content[1])  #输入密码
        wd.find_element_by_id("login").click()                  #点击登录

        #这里你要是想让他不匹配时程序退出，可以写成assert unicode("您的用户名和密码不匹配", "utf-8") not in wd.page_source
        #"您的用户名和密码不匹配"是人人登录失败时的提醒，你要看你们失败时提醒啥把这里改了
        #或者用其他条件判断，wd.page_source是新页面内容，你可以对比新老页面什么差异做判断，这样比较保险
        #因为输入错误提示句在正常页面他可能也会存在
        if unicode("您的用户名和密码不匹配", "utf-8") in wd.page_source:
            print "fail..."
            print unicode("您的用户名和密码不匹配", "utf-8")
            print wd.page_source
        time.sleep(10)
        wd.close()

def get_id_psw_from_file(path):
    """
    读文件，返回一个序列。序列里每个元素是需要输入的内容的序列
    param: path
    return: [["id1","pw1"], ["id2", "pw2"]...]
    """
    return [["id1","pw1"], ["id2", "pw2"]]

if __name__ == "__main__":
    #path是放用户名密码的文件路径
    path = ""
    test_clientid_psw(path)
