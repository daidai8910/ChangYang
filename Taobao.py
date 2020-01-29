# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 2019/03/16
# 淘宝秒杀脚本，扫码登录版
from selenium import webdriver
import datetime
import time

def login(login_method):
    # 打开淘宝登录页，并进行扫码登录
    #2020-01-27 改造为密码登录-滑块无法模拟
    #1-扫码登录 2-用户密码登录
    browser.get("https://www.taobao.com")
    time.sleep(1)
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()

    if login_method == 1: #扫码
        print("请在15秒内完成扫码")
        time.sleep(15)
    elif login_method == 2 : #密码 - 滑块暂时无法解决
            if browser.find_element_by_link_text("密码登录"):
                browser.find_element_by_link_text("密码登录").click()
                browser.find_element_by_id("TPL_username_1").send_keys('daidai8910')
                browser.find_element_by_id('TPL_password_1').send_keys('taobao8910')
                browser.find_element_by_id('J_SubmitStatic').click()
    else:
        print("登录方式错误!!")

    browser.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))

def buy(dead_line):
    # 点击购物车里全选按钮
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now >= dead_line:
            # 点击 全选
            while True:
                try:
                    if browser.find_element_by_id("J_SelectAll2"):
                        browser.find_element_by_id("J_SelectAll2").click()
                        now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print("全选勾选成功 时间 : %s" % now1)
                        break
                except:
                    now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                    print("找不到全选 : %s" % now1)
            # 点击 结算
            while True:
                try:
                    if browser.find_element_by_link_text("结 算"):
                        browser.find_element_by_link_text("结 算").click()
                        now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print("结算点击成功 时间 : %s" % now1)
                        break
                except:
                    pass
            # 点击 提交订单
            while True:
                try:
                    if browser.find_element_by_link_text('提交订单'):
                        now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print("提交订单 时间 : %s" % now1)
                        browser.find_element_by_link_text('提交订单').click()
                        now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print("提交订单成功 时间 : %s" % now1)
                        return 0
                except:
                    now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                    print("再次尝试提交订单 : %s" % now1)
            time.sleep(0.005) #间隔5毫秒

if __name__ == "__main__":
    #times = input("请输入抢购时间，格式如(2018-09-06 11:20:00.000000):")
    # 时间格式："2018-09-06 11:20:00.000000"
    dead_line="2020-01-27 20:43:00.000000"
    browser = webdriver.Chrome(executable_path=r"C:\Users\增宝\AppData\Local\Programs\Python\Python38\Scripts\chromedriver.exe")
    browser.maximize_window()
    login_method = 1
    login(login_method)
    #choose = int(input("到时间自动勾选购物车请输入“1”，否则输入“2”："))
    buy(dead_line)
