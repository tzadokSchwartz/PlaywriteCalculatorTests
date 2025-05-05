from playwright.sync_api import Page
from pages.base_page import BasePage

class Header(BasePage):
    _SETTINGS_BTN = ".bar-menu>.mtt-only-authorized"

    def __init__(self, page: Page):
        super().__init__(page)

    def click_on_settings(self) -> None:
        self.click(self._SETTINGS_BTN)