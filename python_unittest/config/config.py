# -*- coding: utf-8 -*-

from appium import webdriver
import re,os

# config配置部分

def driver_app(self):
    desired_caps = {}
    # 读取设备 id
    readDeviceId = list(os.popen('adb devices').readlines())
    # 正则表达式匹配出 id 信息
    deviceName = re.findall(r'^\w*\b', readDeviceId[1])[0]
    # 读取设备系统版本号
    deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
    platformVersion= deviceAndroidVersion[0].replace('\n','')

    desired_caps['automationName'] = 'Appium'
    desired_caps['deviceName'] = deviceName
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = platformVersion
    desired_caps['noReset'] = True
    desired_caps['sessionOverride'] = True
    desired_caps['unicodeKeyboard'] = True  # 使用unicode编码方式发送字符串
    desired_caps['resetKeyboard'] = True    # 屏蔽软键盘
    desired_caps["appPackage"] = "com.tencent.mm"
    desired_caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(3)
    return driver

