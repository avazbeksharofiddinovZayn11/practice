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

# try avoid thse
people = "Andrew", "John"
animals = "dog",

print("===== Unpacking arguments =====")
groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, *z) = groups
print(f"the x: {x} and y: {y}")
print("z:", z)

# *args > tuple


def calculate(*args):
    print("*args:", args)
    total = 1
    for x in args:
        total *= x
        # print(f"the type(args) value: {type(args)}")
        print(f"the total value: {total}")
        return total

    # Call
calculate(2, 5, 83, 93)
calculate(0, 5, 567)
print("------")
calculate(7, 9)

# **kwargs > divtionary
def introduce(**kwargs):
    print(f"the type(**kwargs) value {type(kwargs)}")
    print(f" Hi I am {kwargs["name"]} and I am {kwargs["age"]} years old!")
    

#call
introduce(name="Justin", age=22)
introduce(name="Shawn", age=30, single=True)

def greeting(*args, **kwargs):
    print("*args >", args)
    print("**kwargs >", kwargs)

#call
greeting("hi", True, 56, name="John", age=22)
