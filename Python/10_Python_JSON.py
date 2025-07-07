# Python JSON
import json

data = { "name": "John Doe", "age": 28, "city": "Houston" }
json_data = json.dumps(data)
print(data)
print(json_data)  # вывод {"name": "John Doe", "age": 28, "city": "Houston"}

a = ['list', 1, 'spisok', 2]

json_data2 = json.dumps(a)
print(json_data2)

# разница в кавычках