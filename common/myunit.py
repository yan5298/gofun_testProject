import  unittest
from common.desired_caps import  appium_desird
import logging
from time import sleep

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('====setUp====')
        self.driver = appium_desird()

    def tearDown(self):
        logging.info('====tearDown===')
        self.driver.close_app()