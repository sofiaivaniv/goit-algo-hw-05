import re
from collections.abc import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    '''Parses the text, finds all real numbers and returns them as a generator.'''
    pattern = r' \d+\.\d+ '
    matches = re.findall(pattern, text)
    for match in matches:
        yield float(match)

def sum_profit(text: str, func: Callable) -> float:
    '''Calculates the total sum of real numbers in the text using a number generator.'''
    gen = func(text)
    sum = 0
    for num in gen:
        sum += num
    return sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")