import pytest
from tests.base_test import BaseTest
from data.test_data import TestData
from utils.math_utils import has_sqr_root_validation

@pytest.mark.usefixtures("setup_page_function")
class TestHasIntSqrRoot(BaseTest):

    @pytest.mark.parametrize("numbers", TestData.numbers_01)
    def test_has_int_sqr_root(self, numbers):
        assert self.calculator_page.has_int_sqr_root(numbers) == has_sqr_root_validation(numbers)

