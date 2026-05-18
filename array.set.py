''' Array & Set
  (1) Array 
  (2) Set
  (3) Specific operators with set
'''
print("===== Array =====")


from array import array
numbers = array("i", [2, 4, 3, 6, 8, 98, 56])
print("numbers(1)", numbers)

numbers.append(100)
numbers.insert(0, 15)
print("numbers(2)", numbers)

numbers.remove(6)
numbers.pop()
print("numbers(3)", numbers)

del numbers[0:2]
print("numbers(4)", numbers)

print("===== Set =====")
