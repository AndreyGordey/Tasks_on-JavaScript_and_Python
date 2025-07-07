# Объекты также могут содержать методы. 
# Методы в объектах — это функции, принадлежащие объекту.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Привет, меня зовут " + self.name)

p1 = Person("Андрей", 52)
p1.myfunc()