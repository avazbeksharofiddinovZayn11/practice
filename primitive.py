print("====== number ======")
# in JAVA , variable is name storage location!
#in Puthon, variable is named reference!

count = 100
count_type = type(count)
print("count:", count, count_type)
print(f"the count: {count} and type {count_type}")

result1 = count.bit_count() # method
result2 = count.numerator # state
print(result1, result2)

print("====== string ======")
# METHODS: upper(), lower(), title(), find(), replace()
course = "AI Python FullStack"
result = type (course)
print(f" the result (1): {result}")

result = course.title()
print(f" the result (2): {result}")

result = course.upper()
print(f" the result (3): {result}")

result = course.replace("FullStack", "MasterClass")
print(f" the result (3): {result}")


print("====== boolean ======")
#Functions: type() input() int() str()

y = input("Give your value fot y:")
print("y:", y)

result = y.isnumeric()
print(f"the input valeu is numeric:, {result}")

# TRUTHY vs FALSE value
#TRUTHY > True 100, -100, "MIT"
# Falsy > False 0, "", None 


test_falsy = "" or 0 or None
print(" the Fasle;", bool(test_falsy))

test_truthy = "MIT" 
print(" the Tuthy;", bool(test_truthy))