import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
 
    pattern = r'\b\d+(\.\d+)?\b'
    matches = re.finditer(pattern, text)
    for match in matches:
        yield float(match.group())

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))

text = "Загальний прибуток складає 100.50, а витрати - 50.25, таким чином чистий прибуток - 50.25"
result = sum_profit(text, generator_numbers)
print(result)
