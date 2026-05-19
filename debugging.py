''' Packges & Debugging
  (1) Python packages & core Package
  (2) package Manager & ExternalPackage
  (3) Debugging
'''
from PIL import Image
import turtle
print("===== Python packages & core Package =====")
''' Python Packages/ modules: Core , File and External
'''
#Core Packages > https://docs.python.org/3/library

# core package
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(2)
# t.circle(100)

# turtle.done()

my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content", content)
finally:
    my_file.close()    

# with
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)

print("DONE")    

print("===== Package Manager & ExternalPackage =====")
# Package Manager (pip) > pip, pipenv npm yarn  composer brew
# External packages > https://pypi.org/


with Image.open("material/your-image.png") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("material/sample.png")

print("=====Debugging =====")

def get_summary(*args): # define
    total_amount = 0
    for a in args:
        total_amount += a
        return total_amount   # solve the bug via debugging

test = 100
result = get_summary(1, 2, 3, 4, 5) #call
print("result:", result)