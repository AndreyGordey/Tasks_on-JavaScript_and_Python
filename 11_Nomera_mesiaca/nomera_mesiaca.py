# Модуль weekday.py

# Словарь для преобразования номеров месяцев в названия
MONTHS = {
    0: "Январь",
    1: "Февраль",
    2: "Март",
    3: "Апрель",
    4: "Май",
    5: "Июнь",
    6: "Июль",
    7: "Август",
    8: "Сентябрь",
    9: "Октябрь",
    10: "Ноябрь",
    11: "Декабрь"
}

# Функция для преобразования номера месяца в название
def month_number_to_name(month_number):
    """Преобразует номер месяца (0-11) в название."""
    if month_number in MONTHS:
        return MONTHS[month_number]
    else:
        raise ValueError("Номер месяца должен быть в диапазоне от 0 до 11.")

# Функция для преобразования названия месяца в номер
def month_name_to_number(month_name):
    """Преобразует название месяца в номер (0-11)."""
    for number, name in MONTHS.items():
        if name.lower() == month_name.lower():
            return number
    raise ValueError("Некорректное название месяца.")
