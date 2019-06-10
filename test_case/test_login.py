from common.myunit import StartEnd
from businessView.loginView import LoginView
import logging,random,unittest,time
import BSTestRunner
class LoginTest(StartEnd):
    def test_phone_login(self):
        logging.info('===start login====')
        r = LoginView(self.driver)

        username = '120000000'+str(random.randint(00,99))

        self.assertTrue(r.login_action(username))
    @unittest.skip('skip test test_phone_login_fail')
    def test_phone_login_fail(self):
        logging.info('===start login====')
        r = LoginView(self.driver)
        time.sleep(30)
        username = '120000000'+str(random.randint(00,99))

        self.assertTrue(r.login_action(username))

if __name__ == '__main__':
    unittest.main()