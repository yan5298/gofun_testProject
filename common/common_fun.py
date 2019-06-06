from baseView.baseView import BaseView
from common.desired_caps import appium_desird
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time,os


class Common(BaseView):
    # cancelBtn = (By.ID, 'android:id/button2')
    # skipBtn = (By.ID, 'com.tal.kaoyan:id/tv_skip')
    #
    # def check_cancelBtn(self):
    #
    #     logging.info('=====check cancelBtn')
    #     try:
    #         cancelBtn = self.find_element(*self.cancelBtn)
    #     except NoSuchElementException:
    #         logging.info('no cancelBtn')
    #     else:
    #         cancelBtn.click()
    #
    # def check_skipBtn(self):
    #     print('check skipbtn')
    #
    #     try:
    #         skipBtn = self.driver.find_element(*self.skipBtn)
    #     except NoSuchElementException:
    #         logging.info('no skipBtn')
    #     else:
    #         skipBtn.click()

    def get_size(self):
        x = self.get_window_size()["width"]
        y = self.get_window_size()["height"]
        return x, y

    def swipeLeft(self):
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x1, y1, x2, y1, 1000)

    def swipeUp(self):
        logging.info('swipeup')
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.95)
        y2 = int(l[0] * 0.35)
        self.swipe(x1, y1, x1, y2, 1000)

    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self, module):

        time=self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module, time)
        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)
        print(image_file)

    # def check_market_ad(self):
    #     logging.info("====check_market_ad====")
    #     try:
    #         element = self.driver.find_element(*self.wemedia_cacel)
    #     except NoSuchElementException:
    #         pass
    #     else:
    #         logging.info('close marker ad')
    #         element.click()

if __name__ == '__main__':
    driver = appium_desird()
    com = Common(driver)
    time.sleep(5)
    # com.check_cancelBtn()
    # time.sleep(5)
    # com.swipeLeft()
    com.getScreenShot('startApp')
