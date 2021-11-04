import json

"""
From JSON string to Python dict
"""

# x = '{ "name":"John", "age":30, "city":"New York"}'
#
# y = json.loads(x)
# print(y)
# print(type(y))
# print(y["age"])

"""
From Python dict to JSON string
"""
py_obj = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(py_obj)
print(y)
print(type(y))
