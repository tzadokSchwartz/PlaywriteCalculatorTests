import math

from playwright.sync_api import Page, Locator
from pages.base_page import BasePage

class CalculatorPage(BasePage):
    _DISPLAY_FIELD = "#display"
    _CLEAR_BTN = "[name='clearButton']"
    _PLUS_BTN = "[name='add']"
    _CALCULATE_BTN = "[name='calculate']"
    _ONE_BTN = "[name='one']"
    _TWO_BTN = "[name='two']"
    _THREE_BTN = "[name='three']"
    _FOUR_BTN = "[name='four']"
    _FIVE_BTN = "[name='five']"
    _SIX_BTN = "[name='six']"
    _SEVEN_BTN = "[name='seven']"
    _EIGHT_BTN = "[name='eight']"
    _NINE_BTN = "[name='nine']"
    _ZERO_BTN = ".button.number[name='zero']"
    _MINUS_BTN = "[name='subtract']"
    _NEGATIVE_BTN = ".button.number[name='negateButton']"
    _DECIMAL_BTN = ".button.number[name='decimal']"
    _MULTIPLY_BTN = "[name='multiply']"
    _DIVIDE_BTN = "[name='divide']"
    _SQR_BTN = "[name='root2']"

    def __init__(self, page: Page):
        super().__init__(page)

    def click_clear(self) -> None:
        self.click(self._CLEAR_BTN)

    def click_plus(self) -> None:
        self.click(self._PLUS_BTN)

    def click_minus(self) -> None:
        self.click(self._MINUS_BTN)

    def click_multiply(self) -> None:
        self.click(self._MULTIPLY_BTN)

    def click_divide(self) -> None:
        self.click(self._DIVIDE_BTN)

    def click_sqr(self):
        self.click(self._SQR_BTN)

    def get_display(self) -> str:
        return self._page.locator(self._DISPLAY_FIELD).input_value().replace(",", "")

    def click_calculate(self) -> None:
        self.click(self._CALCULATE_BTN)

    def type_number(self, number: float) -> None:
        # Simulate typing a number (integer or float) on the calculator UI
        number_str = str(number)
        count = len(number_str)
        negative_number_flag = False
        for i in range(count):
            match number_str[i]:
                case "1":
                    self.click(self._ONE_BTN)
                case "2":
                    self.click(self._TWO_BTN)
                case "3":
                    self.click(self._THREE_BTN)
                case "4":
                    self.click(self._FOUR_BTN)
                case "5":
                    self.click(self._FIVE_BTN)
                case "6":
                    self.click(self._SIX_BTN)
                case "7":
                    self.click(self._SEVEN_BTN)
                case "8":
                    self.click(self._EIGHT_BTN)
                case "9":
                    self.click(self._NINE_BTN)
                case "0":
                    self.click(self._ZERO_BTN)
                case "-":
                    negative_number_flag = True
                case ".":
                    self.click(self._DECIMAL_BTN)
        if negative_number_flag:
            self.click(self._NEGATIVE_BTN)

    def add_numbers(self,  numbers: list[float]) -> float:
        # Add a list of numbers sequentially and return the result
        self.click_clear()
        count = len(numbers)
        for i in range(count):
            number = numbers[i]
            self.type_number(number)
            if i != count - 1:
                self.click_plus()
        self.click_calculate()
        return float(self.get_display())

    def subtract_numbers(self,  numbers: list[float]) -> float:
        # Subtract a list of numbers sequentially and return the result
        self.click_clear()
        count = len(numbers)
        for i in range(count):
            number = numbers[i]
            self.type_number(number)
            if i != count - 1:
                self.click_minus()
        self.click_calculate()
        return float(self.get_display())

    def multiply_numbers(self,  numbers: list[float]) -> float:
        # Multiply a list of numbers sequentially and return the result
        self.click_clear()
        count = len(numbers)
        for i in range(count):
            number = numbers[i]
            self.type_number(number)
            if i != count - 1:
                self.click_multiply()
        self.click_calculate()
        return float(self.get_display())

    def divide_numbers(self,  numbers: list[float]) -> float:
        # Divide a list of numbers sequentially and return the result
        self.click_clear()
        count = len(numbers)
        for i in range(count):
            number = numbers[i]
            if number == 0 and i > 0:
                raise ZeroDivisionError("division by zero")
            self.type_number(number)
            if i != count - 1:
                self.click_divide()
        self.click_calculate()
        return float(self.get_display())

    def has_int_sqr_root(self, number: int) -> bool:
        # Return True if the number has an integer square root, else False
        if number < 0:
            return False
        self.click_clear()
        self.type_number(number)
        self.click_sqr()
        result = float(self.get_display())
        return result.is_integer()

    def is_prime_number(self, number: int) -> bool:
        # Return a list of prime factors for the given number (empty if < 2)
        if number < 2:
            return False
        count = int(math.sqrt(number)) + 1
        for i in range(2, count):
            self.click_clear()
            self.type_number(number)
            self.click_divide()
            self.type_number(i)
            self.click_calculate()
            result = float(self.get_display())
            if math.isclose(result, round(result), rel_tol=1e-9):
                return False
        return True

    def get_prime_factors(self, number: int) -> list[int]:
        if number < 2:
            return []
        prime_factors_list = []
        self.click_clear()
        self.type_number(number)
        self.click_sqr()
        check_limit = float(self.get_display())
        self.click_clear()
        self.type_number(number)
        self.click_divide()
        self.type_number(2)
        self.click_calculate()
        result = float(self.get_display())
        while result.is_integer():
            prime_factors_list.append(2)
            number //= 2
            self.click_clear()
            self.type_number(number)
            self.click_divide()
            self.type_number(2)
            self.click_calculate()
            result = float(self.get_display())
        prime_factor = 3
        while prime_factor <= check_limit:
            self.click_clear()
            self.type_number(number)
            self.click_divide()
            self.type_number(prime_factor)
            self.click_calculate()
            result = float(self.get_display())
            while result.is_integer():
                prime_factors_list.append(prime_factor)
                number //= prime_factor
                self.click_clear()
                self.type_number(number)
                self.click_divide()
                self.type_number(prime_factor)
                self.click_calculate()
                result = float(self.get_display())
            prime_factor += 2
        if number > 2:
            prime_factors_list.append(number)
        return prime_factors_list










