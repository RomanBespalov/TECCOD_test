import math


# 1
def unique_numbers(lst):
    """Функция, которая принимает на вход список целых чисел
    и возвращает новый список, содержащий только уникальные элементы
    из исходного списка."""
    return list(set(lst))


# 2
def prime_numbers(x, y):
    """Функция, которая принимает на вход два целых числа (минимум и максимум)
    и возвращает список всех простых чисел в заданном диапазоне."""
    prime_list = []
    for i in range(max(2, x), y + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime and i != 1:
            prime_list.append(i)
    return prime_list


# 3
class Point:
    """Класс точки в двумерном пространстве"""

    def __init__(self, x, y):
        """Инициализации координат точки"""
        self.x = x
        self.y = y

    def distance_calculation(self, obj2):
        """Вычисление расстояния до другой точки"""
        return math.sqrt((abs(self.x - obj2.x))**2 + (abs(self.y - obj2.y))**2)

    def get_location(self):
        """Получение координат"""
        return self.x, self.y

    def change_location(self, x, y):
        """Изменение координат"""
        self.x = x
        self.y = y


# 4
def sort_by_length(strings):
    """Функция для сортировки строк по возрастанию и убыванию"""
    # Сортируем список по возрастанию длины строк
    strings.sort(key=len)
    print(f"По возрастанию длины:\n{strings}")

    # Сортируем список по убыванию длины строк
    strings.sort(key=len, reverse=True)
    print(f"По убыванию длины:\n{strings}")
