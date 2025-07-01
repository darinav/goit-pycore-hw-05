from typing import Callable
import re

pattern = re.compile(r'(?<=\s)-?\d+(?:\.\d+)?(?=\s)')

def generator_numbers(input_text: str):
    for match in re.findall(pattern, input_text):
        yield float(match)

def sum_profit(input_text: str, func: Callable):
    return sum(func(input_text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")