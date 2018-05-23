#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os

# ================================ 滑动操作 始================================
def swipeUp(driver, t, n):
    '''向上滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5     # x坐标
    y1 = l['height'] * 0.75   # 起始y坐标
    y2 = l['height'] * 0.25   # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

def swipeDown(driver, t, n):
    '''向下滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5          # x坐标
    y1 = l['height'] * 0.25        # 起始y坐标
    y2 = l['height'] * 0.75         # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2,t)

def swipeLeft(driver, t, n):
    '''向左滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.75
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.05
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)

def swipeRight(driver, t, n):
    '''向右滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.05
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)
# ============================ 滑动操作 终================================

# ============================ 截图 始================================
#截图
def getScreenShot(self):
    nowTime = time.strftime("%Y%m%d.%H.%M.%S")
    if not os.path.exists("../../error_picture"):
        os.makedirs("../../error_picture")
    filename = "../../error_picture/%s.jpg" %nowTime
    self.get_screenshot_as_file(filename)
    return True

# 截图 driver.get_screenshot_as_base64()这个方法保存的是base64的编码格式，在HTML界面输出截图的时候，会用到
def add_img(self):
    self.imgs.append(self.driver.get_screenshot_as_base64())
    return True

# ============================ 截图 终================================