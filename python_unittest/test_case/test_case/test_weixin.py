# coding=utf-8
from time import sleep
import unittest
from config.config import driver_app
from encapsulation.encapsulation import *


class SearchTest(unittest.TestCase):
    # 初始化测试环境
    def setUp(self):
        self.driver = driver_app(self)
        self.imgs = []

    def test_case(self):
        try:
            driver = self.driver

            # 点击通讯录
            driver.find_element_by_xpath("//*[@class='android.widget.RelativeLayout'][2]").click()
            # 公众号
            driver.find_element_by_id("com.tencent.mm:id/x_").click()
            # 进入接口测试号
            driver.find_element_by_id("com.tencent.mm:id/z1").click()
            # 热销理财产品
            driver.find_element_by_xpath("//android.widget.TextView[@text='热销理财产品']").click()

            #净值类
            # find_element_by_accessibility_id  => content-desc
            driver.find_element_by_accessibility_id("净值类").click()
            driver.find_element_by_xpath("//android.view.View[8]/android.view.View[2]").click()

            # 向上滑动
            sleep(5)
            swipeUp(driver,1000,1)

            # 分享
            driver.find_element_by_xpath("//android.view.View[7]/android.view.View[27]").click()

            # 立即分享
            driver.find_element_by_xpath("//android.view.View[7]").click()
            driver.find_element_by_id("com.tencent.mm:id/hi").click()
            driver.find_element_by_xpath("//android.widget.LinearLayout[2]").click()

            # 发布
            driver.find_element_by_id("com.tencent.mm:id/hh").click()
        except Exception as e:
            add_img(self)
            getScreenShot(self.driver)
            raise

    # 还原测试环境
    def tearDown(self):
        self.driver.quit()

# 执行测试用例
if __name__ == '__main__':
    unittest.main()