''' CLASS deep diving 
(1) ENCAPSULATION
(2) INHERTENCE
(3) POLIMORPHISM
'''

print("===== INHERTENCE =====")
# PARENT & CHILD
#Parent only parovides only public & protected properties(state+ method) to children!


class Animal:  # Parent
    # state
    description = "the class creates animals"

    # constructor
    def __init__(self, voice):
        self._status = "animal is alive"
        self.voice = voice

    # method
    def make_voice(self):
        print(f"the animal can make voice ; {self.voice}")


class Dog(Animal):
    # state

    # constructor
    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("yes , I can protect you")

    def make_voice(self):
        print(f"the {self.name} says; {self.sound}")    


class Cat(Animal):  # child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):  # child

    # state

    # constructor
    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        pass


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "meyov", True)
fish = Fish("Nemo", "zzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("---------")
dog.make_voice()
fish.make_voice()


print("---------")
print(Dog.description)


print(dog.voice, fish.voice)
print("dog.status|", dog._status)
print("cat.status|", cat._status)


print("===== POLIMORPHISM =====")
dog.make_voice()
fish.make_voice()

print("---------")
# fish > Fish > Animal > object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT", object)
result = a and b and c and d 
print(f"the result:, {result}")

# Fish > Animal . object
data = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data:", data, data2)