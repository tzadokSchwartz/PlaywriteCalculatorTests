import pytest
from tests.base_test import BaseTest
from data.test_data import TestData
from utils.math_utils import add_validation, subtract_validation, multiply_validation, divide_validation

@pytest.mark.usefixtures("setup_page_function")
class TestArithmetic(BaseTest):

    @pytest.mark.parametrize("list_numbers", TestData.list_numbers)
    def test_add_numbers(self, list_numbers):
        assert round(self.calculator_page.add_numbers(list_numbers), 10) == round(add_validation(list_numbers),10), f"Mismatch for numbers: {list_numbers}"

    @pytest.mark.parametrize("list_numbers", TestData.list_numbers)
    def test_subtract_numbers(self, list_numbers):
        assert round(self.calculator_page.subtract_numbers(list_numbers), 10) == round(subtract_validation(list_numbers), 10), f"Mismatch for numbers: {list_numbers}"

    @pytest.mark.parametrize("list_numbers", TestData.list_numbers)
    def test_multiply_numbers(self, list_numbers):
        assert round(self.calculator_page.multiply_numbers(list_numbers), 10) == round(multiply_validation(list_numbers), 10), f"Mismatch for numbers: {list_numbers}"

    @pytest.mark.parametrize("list_numbers", TestData.list_numbers)
    def test_divide_numbers(self, list_numbers):
        assert round(self.calculator_page.divide_numbers(list_numbers), 10) == round(divide_validation(list_numbers), 10), f"Mismatch for numbers: {list_numbers}"