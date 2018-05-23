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
        sleep(3)
    def test_case2(self):
        driver = self.driver

        try:
            # 点击通讯录
            driver.find_element_by_xpath("//*[@class='android.widget.RelativeLayout'][2]").click()

            # 是否进入通讯录--断言---公众号

            # 公众号
            gzh = driver.find_element_by_xpath("//android.widget.TextView[@text='公众号']").text
            self.assertEqual(gzh,u'公众号1',u'未找到“公众号”')

            # assertEqual：如两个值相等，则pass
            # assertNotEqual：如两个值不相等，则pass

        except Exception as e:
            add_img(self)
            getScreenShot(self.driver)
            raise

    def test_case1(self):
        driver = self.driver

        try:
            # 点击通讯录
            driver.find_element_by_xpath("//*[@class='android.widget.RelativeLayout'][2]").click()

            # 是否进入通讯录--断言---公众号

            # 公众号
            gzh = driver.find_element_by_xpath("//android.widget.TextView[@text='公众号']").text
            self.assertEqual(gzh,u'公众号1',u'未找到“公众号”')

            # assertEqual：如两个值相等，则pass
            # assertNotEqual：如两个值不相等，则pass

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