from helpers import web_element
import time
# Locators

success_add = '//div[@id="cart-add-success"]'
btn_add_to_card = '//input[@id="product-orderbutton"]'
btn_cont_shop = '//button[text()="Continue Shopping"]'
btn_cart = '//a[@id="cart-click"]'
prices = '//div[@class="col-xs-3 editorial text-right"]' # [0] == Price
subtotal = '//div[@id="cart-contents-subtotal"]'
first_size = '//*[@id="sizeBox"]/ul/li[1]/sku-detail/a'
checkbox_size = '//a[text()=" Select a Size"]'
# checkbox_size = '//div[@class="product-options"]'


class Snbd_descr(web_element.Base):
    def snbd_buy(self):
        # import pdb;pdb.set_trace()
        try:
            self.return_elements(checkbox_size)
        except Exception:
            self.return_element(btn_add_to_card).click()
            if "PRODUCT ADDED!" == self.return_element(success_add).text:
                self.return_element(btn_cont_shop).click()
        else:
            self.return_element(checkbox_size).click()
            self.return_element(first_size).click()
            self.return_element(btn_add_to_card).click()
            if "PRODUCT ADDED!" == self.return_element(success_add).text:
                self.return_element(btn_cont_shop).click()

    def press_btn_cart(self):
        time.sleep(1)
        self.return_element(btn_cart).click()

    def count_sum(self):
        p = self.return_elements(prices)
        s = self.return_element(subtotal)
        p1 = float(p[1].text[1:])
        p2 = float(p[2].text[1:])

        sum = float(s.text[1:])
        # import pdb;pdb.set_trace()

        if p1+p2 == sum:
            return True

