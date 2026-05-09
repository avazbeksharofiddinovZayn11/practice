''' FUNCTION
(1) DEFINE vs CALL
(2) Parameter vs Argument 
(3) Keyword vs default arguments
(4) Scope
'''

print("===== DEFINE vs CALL =====")
# build in function > print() type()
# Function - Malum bir mantiqni amalga oshiruvchi code block
# Instead of block {} in JAVA , Python uses indentation!

#Define - parameter
def greet(a):
    print(f"How do you do, {a}")

def greeting(b):
    print("greeting is executed")
    return f"hi {b}"


#call - argument
result1 = greet('Zayn')
print("result1", result1)

result2 = greeting("Justin")
print("result2", result2)