import pytest
from playwright.sync_api import Page
from utils.config_reader import ConfigReader
from pages.calculator_page import CalculatorPage

@pytest.fixture(scope="function")
def setup_page_function(request, page: Page):
    url = ConfigReader.read_config("global", "url")
    page.goto(url)
    request.cls.calculator_page = CalculatorPage(page)  # פה נשמר CalculatorPage ב-self.calculator_page
    yield
    page.close()






