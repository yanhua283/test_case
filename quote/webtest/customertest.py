from quote.webpage.customerpage import CustomerPage
from quote.base.usebrowser import UserBrowser
import unittest
class CustomerCase(unittest.TestCase):
    def setUp(self) -> None:
        self.cp = CustomerPage()

    def test_customer_add_only_id(self):
        self.cp.customer_add(id = 's001')
        self.assertEqual(self.cp.get_add_success_text(),'添加记录成功！\n本窗口将在3秒后自动关闭')

    def test_customer_add_id_name(self):
        pass

    def tearDown(self) -> None:
        UserBrowser.quit()

if __name__ == '__main__':
    unittest.main()