from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:
    def __init__ (self):
        self.wd = WebDriver(capabilities={"marionette": False},
                            firefox_binary="C:/Program Files (x86)/Mozilla Firefox ESR/firefox.exe")
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://law-7/addressbook/")

    def destroy(self):
        self.wd.quit()