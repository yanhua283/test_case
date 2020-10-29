from quote.base.usebrowser import UserBrowser
from quote.base.broweroperation import BrowserOperation
from quote.webpage.loginpage import LoginPage
from HTMLTestRunner import HTMLTestRunner
from quote.config.auto_log import Autolog
import unittest
import time

class LoginTest(unittest.TestCase):

    def setUp(self) -> None:
        self.login = LoginPage()
        self.bo = BrowserOperation(UserBrowser.driver)
        self.log = Autolog()

    def test_login_username_password_null(self):
        self.login.login('','')
        self.log.set_mes('输入用户名和密码','info')
        login_error_text = self.bo.get_text('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[5]/td')
        self.assertEqual('请勿非法登录！',login_error_text)

    def test_login_success(self):
        self.login.login('admin','123456')
        correct_text = self.login.login_correct_text('main','/html/body/table/tbody/tr[1]/td/span')
        self.assertEqual('欢迎使用报价管理系统',correct_text)

    def tearDown(self) -> None:
        UserBrowser.quit()

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    suite.addTests(test_case)
    data_now = time.strftime('%y-%m-%d', time.localtime())
    with open('../../report/report_' + data_now + '.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title='auto_test', description='ui_auto_test')
        runner.run(suite)