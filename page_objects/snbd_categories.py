from helpers import web_element

# Locators
category_snbd = "(//div[@class='category-name'])[1]"
first_srch_result = "(//div[@class='category-product-title'])[1]"


class Snowboard(web_element.Base):
    def first_category(self):
        return self.return_element(category_snbd).text

    def srch_rslt(self):
        return self.return_element(first_srch_result).text



