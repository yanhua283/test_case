import time
from quote.base.usebrowser import UserBrowser
from quote.base.broweroperation import BrowserOperation


class LoginPage:

    def __init__(self):
        self.ub = UserBrowser()
        self.bo = BrowserOperation(UserBrowser.driver)
        self.bo.open_url('http://localhost:8080/JavaPrj_6/')

    def login(self,username,password):
        self.bo.send_keys('//*[@id="UserName"]',username)
        self.bo.send_keys('//*[@id="Password"]',password)
        self.bo.click_element('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[6]/td/input[1]')

    def login_correct_text(self,frame_name,xpath):
        self.bo.change_frame(frame_name)
        return self.bo.get_text(xpath)

# if __name__ == '__main__':
#     lp  = LoginPage()
#     lp.login()
#     time.sleep(4)
#     UserBrowser.quit()
