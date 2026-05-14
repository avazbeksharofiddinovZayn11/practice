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
