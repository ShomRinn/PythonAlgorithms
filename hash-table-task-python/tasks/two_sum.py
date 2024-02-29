"""Template for programming assignment: two sum problem."""
from typing import List, Tuple


def find_target_sum(values: List[int], target: int) -> Tuple[int, int]:
    value_to_index = {}  # Хеш-таблица для хранения значений и их индексов

    for i, num in enumerate(values):
        complement = target - num  # Вычисляем дополнение текущего числа до целевой суммы
        if complement in value_to_index:
            return (value_to_index[complement], i)  # Нашли пару, возвращаем индексы
        value_to_index[num] = i  # Сохраняем число и его индекс в хеш-таблицу

    raise ValueError("No two sum solution")

