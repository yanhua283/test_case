import time

from selenium import webdriver

class UserBrowser:

    driver = None

    def __init__(self):
        self.driver = webdriver.Chrome('../chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        UserBrowser.driver = self.driver

        self.driver.switch_to.parent_frame()

    @classmethod
    def quit(cls):
        UserBrowser.driver.quit()

# if __name__ == '__main__':
#     ub = UserBrowser()
#     time.sleep(4)
#     UserBrowser.quit()
