from allure_commons.types import AttachmentType
from helpers.web_element import Fixture
import allure
import pytest


@pytest.fixture
def dr():
    print("setup")
    browser = Fixture()
    yield browser
    print("teardown")
    browser.destroy()


def pytest_exception_interact(node, call, report):
    browser = node.funcargs.get("dr")
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=AttachmentType.PNG
    )


# @pytest.fixture()
# def driver(request):
#     browser = Driver().driver
#     browser.fullscreen_window()
#
#     def fin():
#         print("teardown")
#         browser.quit()
#
#     request.addfinalizer(fin)
#     return browser  # provide the fixture value





