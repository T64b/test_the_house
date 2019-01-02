from page_objects import home_page
from page_objects import snowboard


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
    page = snowboard.Snowboard(dr)
    # import pdb;pdb.set_trace()
    assert "Snowboard" in page.first_category()


def test_srch(dr):
    dr.driver.get('https://www.the-house.com')
    page = home_page.Home(dr)
    snbd_page = page.search_item()
    item = snbd_page.srch_rslt()
    # import pdb;pdb.set_trace()

    assert "Snowboard" in item







