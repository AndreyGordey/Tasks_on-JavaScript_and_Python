class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        # Базовый метод, который будет переопределён в подклассах
        raise NotImplementedError("Каждое животное должно определить свой звук!")
    def introduce(self):
        # Этот метод использует speak(), но не знает, как именно он реализован
        return f"Меня зовут {self.name}, и я говорю {self.speak()}"

class Dog(Animal):
    def speak(self):
        return "гав!"  # Собаки лают

class Cat(Animal):
    def speak(self):
        return "мяу!"  # Кошки мяукают

# Создаём животных и вызываем один и тот же метод
dog = Dog("Бобик")
cat = Cat("Мурка")
print(dog.introduce())  # Меня зовут Бобик, и я говорю гав!
print(cat.introduce())  # Меня зовут Мурка, и я говорю мяу!


# Импортируйте модуль datetime и отобразите текущую дату:
import datetime
x = datetime.datetime.now()
print(x)