''' Tuple
  (1) What is tuple: typle va list  
  (2) Unpacking arguments
  (3) zip
'''

print("=====  What is tuple: typle va list   =====")
# java/PHP NodeJS array => Python list 
# literal 
numbs = [2, 6, 34, 87]
print(numbs)
# constractor
letters = list("Hello World!")
print(letters)

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[3] = "cherry"
print("before fruits:", fruits)

animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "brid"
