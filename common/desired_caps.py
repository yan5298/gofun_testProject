import logging
import logging.config
from appium import webdriver
import yaml
import time
import os

CON_LOG = '../config/log.conf'
# logging.config.fileConfig(CON_LOG)
logging.basicConfig()
logging = logging.getLogger()

def  appium_desird():

    with open('../config/gofun_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file)

    desired_caps={}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['platformName']

    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', data['appname'])

    desired_caps['app'] = app_path
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']

    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    logging.info("start app...")
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
    driver.implicitly_wait(15)
    return driver
    driver.implicitly_wait(15)
    time.sleep(20)


if __name__ == '__main__':
    appium_desird()


