# Функция reverseArray возвращает новый массив с обратным порядком элементов
def reverseArray(array):
    return array[::-1]  # Используем срез для получения обратного массива

# Функция reverseArrayInPlace меняет порядок элементов в исходном массиве
def reverseArrayInPlace(array):
    left = 0  # Индекс начала массива
    right = len(array) - 1  # Индекс конца массива

    # Меняем элементы местами, пока не дойдём до середины массива
    while left < right:
        # Меняем элементы местами
        array[left], array[right] = array[right], array[left]
        # Сдвигаем индексы
        left += 1
        right -= 1

# Пример использования
original_array = [1, 2, 3, 4, 5]

# Используем reverseArray
reversed_array = reverseArray(original_array)
print("Новый массив с обратным порядком:", reversed_array)  # [5, 4, 3, 2, 1]

# Используем reverseArrayInPlace
reverseArrayInPlace(original_array)
print("Исходный массив после изменения:", original_array)  # [5, 4, 3, 2, 1]
