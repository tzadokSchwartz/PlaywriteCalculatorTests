import random

import pytest
from tests.base_test import BaseTest
from data.test_data import TestData

@pytest.mark.usefixtures("setup_page_function")
class TestLists(BaseTest):

    def test_delete_all_lists(self):
        self.main_page.add_list(random.choice(TestData.valid_names))
        self.main_page.delete_all_lists()
        assert self.main_page.validate_no_lists_exist()

    @pytest.mark.parametrize("list_valid_name", TestData.valid_names)
    def test_add_list_with_valid_names(self, list_valid_name):
        self.main_page.add_list(list_valid_name)
        assert self.main_page.is_list_exist(list_valid_name)

    # @pytest.mark.parametrize("list_invalid_name", TestData.list_invalid_names)
    # def test_add_list_with_invalid_names(self, list_invalid_name):
    #     self.main_page.add_list(list_invalid_name)
    #     assert not self.main_page.validate_list_name_exists(list_invalid_name)

    def test_delete_list(self):
        random_name = self.main_page.random_name()
        self.main_page.add_list(random_name)
        self.main_page.delete_list(random_name)
        assert not self.main_page.is_list_exist(random_name)

    @pytest.mark.parametrize("list_valid_name", TestData.valid_names)
    def test_rename_list_with_valid_names(self, list_valid_name):
        valid_list_name = random.choice(TestData.valid_names)
        self.main_page.add_list(valid_list_name)
        self.main_page.rename_list(valid_list_name, list_valid_name)
        assert self.main_page.is_list_exist(list_valid_name)

    # @pytest.mark.parametrize("list_invalid_name", TestData.list_invalid_names)
    # def test_rename_list_with_invalid_names(self, list_invalid_name):
    #     valid_list_name = random.choice(TestData.list_valid_names)
    #     self.main_page.add_list(valid_list_name)
    #     self.main_page.rename_list(valid_list_name, list_invalid_name)
    #     assert not self.main_page.validate_list_name_exists(list_invalid_name)

    def test_hide_list(self):
        random_name = self.main_page.random_name()
        self.main_page.add_list(random_name)
        self.main_page.hide_list(random_name)
        assert self.main_page.is_list_hidden(random_name)

    def test_unhide_list(self):
        random_name = self.main_page.random_name()
        self.main_page.add_list(random_name)
        self.main_page.hide_list(random_name)
        self.main_page.click_on_menu_list(random_name)
        assert self.main_page.is_list_exist(random_name)

    def test_click_on_list_from_main_page(self):
        random_name = self.main_page.random_name()
        self.main_page.add_list(random_name)
        self.main_page.click_on_list(random_name)
        assert self.main_page.is_list_selected(random_name)

    def test_click_on_list_from_tabs_menu(self):
        random_name = self.main_page.random_name()
        self.main_page.add_list(random_name)
        self.main_page.click_on_menu_list(random_name)
        assert self.main_page.is_list_selected(random_name)
