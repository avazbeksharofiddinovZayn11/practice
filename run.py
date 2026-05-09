# Dunder __builtins__, __init__

massage = "PYTHON: Everything is object"
print(massage)

result = type(massage)
print("result:", result)

''' In Python , there are builtin tools:
(1) TYPES: int, float, str, list, dict
(2) FUNCTIONS: print() len() input() type() str() int()
CONSTANTS: True, False, None
'''

print(dir(__builtins__))