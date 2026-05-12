''' OBLECTS
  (1) What is object
  (2) Iterable objects & RANGE 
  (3) DICTIONARY
  (4) error handling system
'''
import array # package
import math 
from math import ceil
print("===== What is object =====")
# An oject has state and method properties
# Everything is object in Python 


print(type("Hello World"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

#paradigma > Function Programing & OOP
# OO 4concepts > Abstraction , Encabshilation , Inheritence Polimophism
result1 = math.ceil(98.6) # call
print("result1", result1)

result2 = ceil(99.6)
print("result2!", result2 )