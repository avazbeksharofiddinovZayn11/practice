''' Packges & Debugging
  (1) Python packages & core Package
  (2) package Manager & ExternalPackage
  (3) Debugging
'''

print("===== Python packages & core Package =====")
''' Python Packages/ modules: Core , File and External
'''
#Core Packages > https://docs.python.org/3/library

# core package
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(2)
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