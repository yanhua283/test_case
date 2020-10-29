import time
# from quote.base.usebrowser import UserBrowser

from selenium import webdriver
class BrowserOperation:

    def __init__(self,driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    def open_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e,'url address error')

    def send_keys(self,xpath,content):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(content)
        except Exception as e:
            print(e,'element not find')

    def click_element(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print(e,'element not find')

    def get_text(self,xpath):
        try:
            text = self.driver.find_element_by_xpath(xpath).text
            return text
        except Exception as e:
            print(e, 'element not find')


    def change_frame(self,frame_name):
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame(frame_name)

    def change_window(self,title):
        for window_hd in self.driver.window_handles:
            self.driver.switch_to.window(window_hd)
            if window_hd.title == title:
                break


# if __name__ == '__main__':
#     ub = UseBrowser()
#     bo = BrowserOperation(UseBrowser.driver)
#     bo.open_url('http://localhost:8080/JavaPrj_6/')
#     bo.send_keys('//*[@id="UserName"]','admin')
#     bo.send_keys('//*[@id="Password"]','admin')
#     bo.click_element('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[6]/td/input[1]')
#     UserBrowser.quit()