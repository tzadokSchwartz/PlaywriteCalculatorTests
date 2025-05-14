import pytest
from tests.base_test import BaseTest
from data.test_data import TestData

@pytest.mark.usefixtures("click_on_list")
class TestTasks(BaseTest):

    @pytest.mark.parametrize("task_valid_name", TestData.valid_names)
    def test_add_valid_task(self, task_valid_name):
        self.main_page.add_task(task_valid_name)
        assert self.main_page.is_task_exist(task_valid_name)

    @pytest.mark.parametrize("task_invalid_name", TestData.invalid_names)
    def test_add_invalid_task(self, task_invalid_name):
        self.main_page.add_task(task_invalid_name)
        assert not self.main_page.is_task_exist(task_invalid_name)

    def test_search_type_task_full_name(self):
        self.main_page.add_multiple_tasks(TestData.task_list_01)
        self.main_page.search_task(TestData.full_task_name_01)
        assert self.main_page.visible_tasks() == [TestData.task_list_01[1]]

    def test_search_task_incorrect_name(self):
        self.main_page.add_multiple_tasks(TestData.task_list_01)
        self.main_page.search_task(TestData.incorrect_task_name_01)
        assert not self.main_page.visible_tasks()

    def test_task_counter(self):
        self.main_page.add_multiple_tasks(TestData.task_list_01)
        assert self.main_page.counter_total_tasks() == self.main_page.visible_tasks_count()

    def test_mark_task(self):
        pass

    def test_unmark_task(self):
        pass

    # def test_add_empty_task(self):
    #     pass
    #
    # def test_mark_a_task(self):
    #     pass
    #
    # def test_mark_multiple_tasks(self):
    #     pass
    #
    # def test_counter_0_when_there_are_no_tasks(self):
    #     pass
    #
    # def test_counter_after_adding_a_task(self):
    #     pass
    #
    # def test_counter_after_adding_multiple_tasks(self):
    #     pass
    #
    # def test_counter_after_deleting_a_task(self):
    #     pass
    #
    # def test_task_id_after_adding_a_task(self):
    #     pass
    #
    # def test_task_id_after_adding_multiple_tasks(self):
    #     pass
    #
    # def test_task_created_time(self):
    #     pass
    #
    # def test_task_completed_time(self):
    #     pass



