''' CLASS
(1) What is class 
(2) ordinary va static propertis
(3) special methods
'''

print("===== What is class =====")

# class = blueprint for object creation!
# structure > state constructor method


class Person():

    # state
    message = "static state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says I am {self.age}!")

    @classmethod
    def explain(cls):
        print("static method property executed!")


person1 = Person("Martin", 35)
person2 = Person("Zayn", 24)
person3 = Person("John", 22)

# ordinary state
print("person1.name:", person1.name)

# ordinary method
person1.introduce()
person2.say_age()


print("===== ordinary va static propertis =====")
# static state 
new_massage = Person.message 
print("new_message:", new_massage)

# static method 
Person.explain()
