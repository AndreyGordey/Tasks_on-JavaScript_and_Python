def isEven(n):
    # Если число отрицательное, преобразуем его в положительное
    if n < 0:
        n = -n
    # Базовые случаи
    if n == 0:
        return True  # Ноль чётный
    elif n == 1:
        return False  # Единица нечётная
    # Рекурсивный случай
    else:
        return isEven(n - 2)

# Тестирование функции
print(isEven(50))  # Ожидается True (чётное)
print(isEven(75))  # Ожидается False (нечётное)
