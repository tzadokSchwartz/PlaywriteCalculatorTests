import pytest

from data.test_data import TestData
from tests.base_test import BaseTest
from utils.math_utils import get_prime_factors_validation

@pytest.mark.usefixtures("setup_page_function")
class TestGetPrimeFactors(BaseTest):

    @pytest.mark.parametrize("numbers", TestData.numbers_01)
    def test_get_prime_factors(self, numbers):
        assert self.calculator_page.get_prime_factors(numbers) == get_prime_factors_validation(numbers)
