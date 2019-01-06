from page_objects import home_page
from page_objects import snbd_categories
from page_objects import snbd_all
from page_objects import snbd_description


def test_title(dr):
    dr.driver.get('https://www.the-house.com')
    page = home_page.Home(dr)
    assert "The House" in page.driver.title


def test_alt_logo(dr):
    dr.driver.get('https://www.the-house.com')
    page = home_page.Home(dr)
    assert "The House" in page.logo_alt_text()


def test_snbd_category(dr):
    dr.driver.get('https://www.the-house.com/boardshop.html')
    page = snbd_categories.Snowboard(dr)
    # import pdb;pdb.set_trace()
    assert "Snowboard" in page.first_category()


def test_srch(dr):
    dr.driver.get('https://www.the-house.com')
    page = home_page.Home(dr)
    snbd_page = page.search_item()
    item = snbd_page.srch_rslt()
    # import pdb;pdb.set_trace()
    assert "Snowboard" in item


def test_shopping_card(dr):
    dr.driver.get('https://www.the-house.com/snbd.html')
    page = snbd_all.Snbd(dr)
    page.close_signup()
    snbd_desc = page.add_snbd_to_buy(0)
    snbd_desc.snbd_buy()
    dr.driver.get('https://www.the-house.com/snbd.html')
    # import pdb;pdb.set_trace()
    snbd_desc = page.add_snbd_to_buy(1)
    snbd_desc.snbd_buy()
    snbd_desc.press_btn_cart()
    assert snbd_desc.count_sum()


def test_logining(dr):





