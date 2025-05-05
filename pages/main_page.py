import random
import string
import time

from playwright.sync_api import Page, Locator
from pages.base_page import BasePage
from pages.components.header import Header

class MainPage(BasePage):
    _LIST = ".mtt-tab:not(#list_all):not(.mtt-tab-hidden)"
    _LIST_ACTION_BTN = ".mtt-tab-selected .list-action"
    _DELETE_LIST_BTN = "#btnDeleteList"
    _MODAL_OK_BTN = "#btnModalOk"
    _ADD_LIST_BTN = ".mtt-tabs-new-button"
    _MODAL_TEXT_FIELD = "#modalTextInput"
    _LIST_TITLE = ".title"
    _RENAME_LIST_BTN = "#btnRenameList"
    _HIDE_LIST_BTN = "#btnHideList"
    _HIDDEN_LIST = ".mtt-tab.mtt-tab-hidden"
    _HIDDEN_LIST_TITLE = ".title"
    _SELECT_LIST_BTN = "#tabs_buttons"
    _MENU_LIST = "[id^='slmenu_list']"
    _MENU_LIST_TITLE = ">a"
    _LIST_SELECTED_TITLE = ".mtt-tab-selected .title"
    _TASK_FIELD = "#task"
    _TASK_SUBMIT_BTN = "#newtask_submit"
    _TASK = ".task-row"
    _TASK_TITLE = ".task-title"
    _SEARCH_FIELD = "#search"


    def __init__(self, page: Page):
        super().__init__(page)
        self._header = Header(page)

    def delete_all_lists(self) -> None:
        list_of_lists = self._page.locator(self._LIST)
        while list_of_lists.count():
            current_list_title = list_of_lists.nth(0).locator(self._LIST_TITLE).inner_text()
            self.delete_list(current_list_title)
            time.sleep(0.5)

    def validate_no_lists_exist(self) -> bool:
        list_of_lists = self._page.locator(self._LIST)
        if not list_of_lists.count():
            return True
        else:
            return False

    def add_list(self, list_name: str) -> None:
        self.click(self._ADD_LIST_BTN)
        self.fill(self._MODAL_TEXT_FIELD, list_name)
        self.click(self._MODAL_OK_BTN)

    def is_list_exist(self, list_name: str) -> bool:
        list_of_lists = self._page.locator(self._LIST)
        count = list_of_lists.count()
        for i in range(count):
            list_title = list_of_lists.nth(i).locator(self._LIST_TITLE).inner_text()
            if list_title == list_name:
                return True
        return False

    def delete_list(self, list_name: str) -> None:
        self.click_on_list(list_name)
        self.click(self._LIST_ACTION_BTN)
        self.click(self._DELETE_LIST_BTN)
        self.click(self._MODAL_OK_BTN)

    def click_on_list(self, list_name: str) -> None:
        list_of_lists = self._page.locator(self._LIST)
        count = list_of_lists.count()
        for i in range(count):
            current_list = list_of_lists.nth(i).locator(self._LIST_TITLE)
            if current_list.inner_text() == list_name:
                current_list.click()
                return
        raise Exception(f"{list_name} was not found")

    def rename_list(self, list_name: str, new_list_name: str) -> None:
        self.click_on_list(list_name)
        self.click(self._LIST_ACTION_BTN)
        self.click(self._RENAME_LIST_BTN)
        self.fill(self._MODAL_TEXT_FIELD, new_list_name)
        self.click(self._MODAL_OK_BTN)

    def hide_list(self, list_name: str) -> None:
        self.click_on_list(list_name)
        self.click(self._LIST_ACTION_BTN)
        self.click(self._HIDE_LIST_BTN)

    def is_list_hidden(self, list_name: str) -> bool:
        hidden_lists = self._page.locator(self._HIDDEN_LIST)
        count = hidden_lists.count()
        for i in range(count):
            hidden_list_title = hidden_lists.nth(i).locator(self._HIDDEN_LIST_TITLE).inner_text()
            if hidden_list_title == list_name:
                return True
        return False

    def click_on_menu_list(self, list_name: str) -> None:
        self.click(self._SELECT_LIST_BTN)
        menu_lists = self._page.locator(self._MENU_LIST)
        count = menu_lists.count()
        for i in range(count):
            menu_list_title = menu_lists.nth(i).locator(self._MENU_LIST_TITLE).inner_text()
            if menu_list_title == list_name:
                menu_lists.nth(i).click()
                return
        raise Exception(f"{list_name} was not found on the tabs menu")

    def random_name(self) -> str:
        letters = "".join(random.choices(string.ascii_uppercase, k=4))
        digits = "".join(random.choices(string.digits, k=2))
        return letters + digits

    def is_list_selected(self, list_name: str) -> bool:
        list_selected_title = self._page.locator(self._LIST_SELECTED_TITLE).inner_text()
        if list_selected_title == list_name:
            return True
        else:
            return False

    def add_task(self, task_name: str) -> None:
        self.fill(self._TASK_FIELD, task_name)
        self.click(self._TASK_SUBMIT_BTN)

    def is_task_exist(self, task_name: str) -> bool:
        tasks = self._page.locator(self._TASK)
        count = tasks.count()
        for i in range(count):
            task_title = tasks.nth(i).locator(self._TASK_TITLE).inner_text()
            if task_title == task_name:
                return True
        return False

    def add_multiple_tasks(self, task_names: list[str]) -> None:
        for task_name in task_names:
            self.add_task(task_name)

    def random_names(self, size: int) -> list[str]:
        name_list = []
        for i in range(size):
            name_list.append(self.random_name())
        return name_list

    def search_task(self, task_name: str) -> None:
        self.type(self._SEARCH_FIELD, task_name)

    def visible_tasks(self) -> list[str]:
        task_names = []
        tasks = self._page.locator(self._TASK)
        count = tasks.count()
        for i in range(count):
            task_title = tasks.nth(i).locator(self._TASK_TITLE).inner_text()
            task_names.append(task_title)
        return task_names








