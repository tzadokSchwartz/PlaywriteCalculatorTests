import math

def add_validation(numbers: list[float]) -> float:
    # Return the sum of the list numbers
    if not numbers:
        raise ValueError("numbers list cannot be empty")
    count = len(numbers)
    result = numbers[0]
    for i in range(1, count):
        result += numbers[i]
    return result

def subtract_validation(numbers: list[float]) -> float:
    # Return the result of subtracting the list numbers
    if not numbers:
        raise ValueError("numbers list cannot be empty")
    count = len(numbers)
    result = numbers[0]
    for i in range(1, count):
        result -= numbers[i]
    return result

def multiply_validation(numbers: list[float]) -> float:
    # Return the result of multiply the list numbers
    if not numbers:
        raise ValueError("numbers list cannot be empty")
    count = len(numbers)
    result = numbers[0]
    for i in range(1, count):
        result *= numbers[i]
    return result

def divide_validation(numbers: list[float]) -> float:
    # Return the result of the division of the list numbers
    if not numbers:
        raise ValueError("numbers list cannot be empty")
    count = len(numbers)
    result = numbers[0]
    for i in range(1, count):
        if numbers[i] == 0:
            raise ZeroDivisionError("division by zero")
        result /= numbers[i]
    return result

def has_sqr_root_validation(number: int) -> bool:
    # Return True if the number has a square root, otherwise False
    if number < 0:
        return False
    result = float(math.sqrt(number))
    return result.is_integer()

def is_prime_number_validation(number: int) -> bool:
    # Return True if the number is prime, otherwise False
    if number < 2:
        return False
    count = int(math.sqrt(number)) + 1
    for i in range(2, count):
        if number % i == 0:
            return False
    return True

def get_prime_factors_validation(number: int) -> list[int]:
    # Return a list of prime factors of the number
    if number < 2:
        return []
    prime_factors_list = []
    while number % 2 == 0:
        prime_factors_list.append(2)
        number //= 2
    prime_factor = 3
    check_limit = math.sqrt(number)
    while prime_factor <= check_limit:
        while number % prime_factor == 0:
            prime_factors_list.append(prime_factor)
            number //= prime_factor
        prime_factor += 2
    if number > 2:
        prime_factors_list.append(number)
    return prime_factors_list
