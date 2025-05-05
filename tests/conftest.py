import pytest
from playwright.sync_api import Page
from utils.config_reader import ConfigReader
from pages.main_page import MainPage

@pytest.fixture(scope="function")
def setup_page_function(request, page: Page):
    request.cls.page = page
    url = ConfigReader.read_config("global", "url")
    request.cls.page.goto(url)
    # page.goto("https://www.mytinytodo.net/demo/#list/1")
    request.cls.main_page = MainPage(request.cls.page)
    yield
    request.cls.page.close()

@pytest.fixture(scope="function")
def click_on_list(setup_page_function, request):
    random_name = request.cls.main_page.random_name()
    request.cls.main_page.add_list(random_name)
    request.cls.main_page.click_on_list(random_name)






