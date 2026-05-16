''' LOOP operators
  (1) for 
  (2) break/else 
  (3) while
'''

print("===== for operators =====")
# Iterable objects > string dict tuple zip list range map filter
text = "MIT"
numbs = [10, 3, 87, 9]
car_obj = dict(brand="Ferrari", year=2025)
range_obj = range(6)

for latter in text:
  print(f"the letter: {latter}")

print("======")
for number in numbs:
    print(f"the number: {number}" )

print("======")
for key in car_obj:
    print(f"the key: {key} => value: {car_obj.get(key)}")


print("===== break/else =====")
for x in range(1, 20, 6):
    print(f"the x: {x}")
    if x > 10:
        print("reached break")
        break
else:
    print(" successfully")    

print("===== while operators =====")
numb = 100
while numb > 0:
    numb -= 10
    print(f"the numb equals {numb}")

print("====")
count = 0
while True:
    count += 1
    x = int(input("find number"))

    if x == 51:
        print(f"you found number in {count} steps")
        break    
    else:
        print("Wrong , please find again")