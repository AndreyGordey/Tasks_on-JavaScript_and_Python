# Наследование позволяет нам определить класс, 
# который наследует все методы и свойства другого класса

# Создайте класс с именем Person, со свойствами firstname и lastname и методом, printname:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Используйте класс Person для создания объекта, а затем выполните метод printname:

x = Person("Щипунов", "Андрей")
x.printname()

print(x)


class Student(Person):
  pass



x = Student("Щипунова", "Татьяна")
x.printname()

print(x)


class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)