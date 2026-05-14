''' OPERATORS & CONDITIONS
(1) Operators
(2) conditions
(3) Logical Operators
'''

print("===== OPERATORS & CONDITIONS =====")
# +, -, >, >=, <, <=, *, /,   //, %, +=, **


a = 34
b = 56
print(a / b)
result = a // b
left = a % b
print(f"the result:, {result} and left: {left}")

a += 100
print("a", a)

print("b**2", b**2)
print("b**3", b**3)
print("="*7)

c = dict(name="Martin", age=35)
d = dict(name="Martin", age=35)
e = c
print("c==d", c == d) # only value
print(id(c), id(d), id(e))


print("c is d", c is d)
print("c is e", c is e)

print("===== Conditions =====")
x = 55

if x > 50:
  print("case A")
elif x > 10:
  print("case B")
else:
  print("Case C")  

print("===== Logical Operators =====")


age = 24

# person = None
# if age > 16:
#   person = "adult"
# else:
#   person = "child"

# print("person:", person)


#Ternary
person = "adult" if age > 18 else "minor"
print("person:", person)

print("-----------")

is_student = True
is_admin = False
is_guest = True
is_parent = True

if not is_student:
  print("Wellcome here , do want to be student!")
elif is_admin:
    print("please go to this offiice!")
elif is_guest or is_parent:
  print("Waiting room is over there !")    
else:
  print("Other cases")      