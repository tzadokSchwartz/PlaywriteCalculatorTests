import pytest
from tests.base_test import BaseTest
from data.test_data import TestData
from utils.math_utils import is_prime_number_validation

@pytest.mark.usefixtures("setup_page_function")
class TestIsPrimeNumber(BaseTest):

    @pytest.mark.parametrize("numbers", TestData.numbers_02)
    def test_is_prime_number(self, numbers):
        assert self.calculator_page.is_prime_number(numbers) == is_prime_number_validation(numbers)
