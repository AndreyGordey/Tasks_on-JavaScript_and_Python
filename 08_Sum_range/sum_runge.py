# Функция range
def range_custom(start, end):
    # Создаем массив чисел от start до end включительно
    return list(range(start, end + 1))

# Функция sum
def sum_custom(numbers):
    # Суммируем все элементы массива numbers
    return sum(numbers)

# Пример использования
start = 1
end = 5

# Генерация диапазона чисел
numbers = range_custom(start, end)
print("Диапазон чисел:", numbers)

# Сумма чисел в диапазоне
result = sum_custom(numbers)
print("Сумма чисел:", result)
print("Sum number:", result)

'''1. Функция range_custom:

   • Использует встроенную функцию range(start, end + 1) для создания последовательности чисел от start до end включительно.

   • Преобразует эту последовательность в список с помощью list().

2. Функция sum_custom:

   • Использует встроенную функцию sum() для вычисления суммы элементов массива.
'''