import time

from quote.webpage.loginpage import LoginPage
from quote.base.broweroperation import BrowserOperation
class CustomerPage:
    def __init__(self):
        self.lp = LoginPage()
        self.lp.login('admin','123456')


    def customer_add(self,**kwargs):
        self.lp.bo.change_frame('Links')
        self.lp.bo.click_element('//*[@id="Bar_panel0_b0"]/img')
        time.sleep(3)
        self.lp.bo.change_frame('main')
        time.sleep(3)
        self.lp.bo.click_element('/html/body/center/table[2]/tbody/tr[2]/td[2]/a')
        self.lp.bo.change_window('新增客户信息')
        self.lp.bo.send_keys('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input',kwargs.get('id', ''))
        self.lp.bo.send_keys('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[4]/input',kwargs.get('name',''))
        self.lp.bo.send_keys('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input',kwargs.get('telephone', ''))
        self.lp.bo.send_keys('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[4]/input',kwargs.get('address', ''))
        self.lp.bo.send_keys('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input',kwargs.get('relationman', ''))
        self.lp.bo.send_keys('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[4]/input',kwargs.get('otherinfo', ''))
        time.sleep(5)
        self.lp.bo.click_element('/html/body/center/form/table[2]/tbody/tr/td/input[1]')

    def get_add_success_text(self):
        self.lp.bo.change_window('添加记录成功')
        customer_add_text = self.lp.bo.get_text('/html/body/center')
        return customer_add_text

    def customer_modify(self):
        pass

if __name__ == '__main__':
    cp = CustomerPage()
    # cp.customer_add(id = 's001',name='tim')
