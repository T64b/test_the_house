from helpers import web_element
from page_objects import snowboard
from selenium.webdriver.common.keys import Keys



# Locators
logo_img = "//a[@class='logo']/img"
nav_items = "//ul[@class='navigation']/li[@class='drop']"
search = "//input[@name='keywords']"
srch_btn = "//button[text()='GO']"
# first_srch_result = "(//*[@class='displayname'])[1]"


class Home(web_element.Base):
    def get_title(self):
        return self.driver.title

    def logo_alt_text(self):
        return self.return_element(logo_img).get_attribute("alt")

    def search_item(self):
        self.return_element(search).send_keys("snowboard")
        self.return_element(srch_btn).send_keys(Keys.ENTER)
        return snowboard.Snowboard(self)



    def press_nav_items(self):
        get_nav_items = self.return_element(nav_items)

