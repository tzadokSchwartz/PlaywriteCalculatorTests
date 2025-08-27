
# Calculator Automation

This project contains automated tests for a web calculator using Selenium/Playwright and Python, following OOP principles and the Page Object Model (POM).

## Tasks Implemented

1. Perform **addition, subtraction, multiplication, and division** on a list of numbers.
2. Check if a number has an **integer square root**.
3. Check if a number is a **prime number**.
4. **Bonus:** Find all **prime factors** of a number using the calculator.

## Project Structure

* **pages/** – Page Objects: `BasePage` for generic actions, `CalculatorPage` for calculator-specific actions and operations.
* **tests/** – Pytest test classes for arithmetic operations, square root, prime check, and prime factors.
* **data/** – Test data for positive, negative, and fractional numbers.
* **utils/** – Validation functions to compare calculator results with expected results.
* **config.ini** – Project configuration (URL, pytest options).

## How to Run

```bash
pip install -r requirements.txt
pytest
```