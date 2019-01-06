from helpers import web_element
from page_objects import snbd_description
import time
# Locators
snowboards = ['(//a[@class="category-product-mainimage clearfix"])[1]',
              '(//a[@class="category-product-mainimage clearfix"])[2]']
success_add = '//div[@id="cart-add-success"]'
btn_add_to_card = '//input[@id="product-orderbutton"]'
btn_close_signup = '(//div[@class="md-content"]/button)[1]'


class Snbd(web_element.Base):
    def close_signup(self):
        self.return_element(btn_close_signup).click()

    def add_snbd_to_buy(self, i):
        self.return_element(snowboards[i]).click()
        return snbd_description.Snbd_descr(self)

        # try:
        #     self.return_element(btn_close_signup)
        # except Exception:
        #     self.return_element(snowboards[i]).click()
        #     return snbd_description.Snbd_descr(self)
        # else:
        #     self.return_element(btn_close_signup).click()


