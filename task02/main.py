import re

def generator_numbers(input_text: str):
    """
    Повертає реальні числа з тексту.

    Args:
        text (str): Вхідний текст з числами.
    
    Yields:
        float: Повертає число з тексту.
    """
    pattern = r"[-+]?\d*\.\d+|\d+"
    for match in re.finditer(pattern, input_text):
        yield float(match.group())


def sum_profit(input_text: str, func):
    """
    Обчислює суму чисeл з вхідного тексту.

    Args:
        text (str): Вхідний текст.
        func (callable): Генератор функція (e.g., generator_numbers).

    Returns:
        float: Сума чисел з тексту.
    """
    total_sum = sum(func(input_text))
    return total_sum        

text = "Загальний дохід працівника складається з декількох частин:\
    1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")