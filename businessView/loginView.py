from baseView.baseView import BaseView
from common.common_fun import Common
from common.desired_caps import appium_desird
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time
import json
import requests

class LoginView(BaseView):
    phone_login = (By.ID, 'lb_phone')

    et_login_phonenum = (By.ID, 'com.guagua.live.testint:id/et_login_phonenum')
    btn_login_sendcode = (By.ID, 'com.guagua.live.testint:id/btn_login_sendcode')
    phonevery = (By.ID, 'com.guagua.live.testint:id/et_login_phonevery')
    btn_login_phone = (By.ID, 'com.guagua.live.testint:id/btn_login_phone')
    # main_type = (By.XPATH, '(//android.widget.ImageView[@content-desc=\"首页\"])[1]')

    def login_action(self, username):
        time.sleep(10)
        logging.info('=======login action====')
        time.sleep(1)
        #选择手机号登录
        self.driver.find_element(*self.phone_login).click()
        time.sleep(2)
        self.driver.implicitly_wait(3)
        # logging.info('username is:%s' %username)
        #输入手机号
        self.driver.find_element(*self.et_login_phonenum).send_keys(username)
        # self.driver.find_element(*self.btn_login_sendcode).send_keys(password)
        self.driver.implicitly_wait(3)
        #点击获取验证码
        self.driver.find_element(*self.btn_login_sendcode).click()
        time.sleep(5)
        #获取验证码
        self.reponse = requests.post("https://m.19gofun.com/cgi/login/test?iwant=code&data=86" + username + "")
        self.ret = json.loads(self.reponse.content.decode())
        self.code = self.ret['content']['code']
        print(self.code)
        #填写验证码
        self.driver.find_element(*self.phonevery).click()
        self.driver.find_element(*self.phonevery).send_keys(self.code)

        #点击登录按钮
        self.driver.find_element(*self.btn_login_phone).click()
        self.driver.implicitly_wait(3)

        logging.info('=======login finshed====')


if __name__ == '__main__':

    driver = appium_desird()
    l = LoginView(driver)
    l.login_action('17600629988')