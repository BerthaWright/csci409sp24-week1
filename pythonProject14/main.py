###

''' Bertha Wright: Lab:Inheritance
Date: 11-Nov-2022
Assignment: Week 11
Pseudocode: None Needed
'''

###


class Pet:
    def __init__(self):
        self.petname = ""

    def set_petname(self, name):
        self.petname = name


class Cat(Pet):
    def __init__(self):
        Pet.__init__(self)
        self.catmood = False

    def mood(self, mood):
        self.catmood = mood
        if self.catmood == "True":
            self.catmood = "This cat is grumpy"
        else:
            self.catmood = "This cat is not grumpy"

    def display_pet(self):
        print("This cat's name is",self.petname, self.catmood)


class Dog(Pet):
    def __init__(self):
        Pet.__init__(self)
        self.dogmood = False

    def mood(self, mood):
        self.dogmood = mood
        if self.dogmood == "True":
            self.dogmood = "This dog is happy."
        else:
            self.dogmood = "This dog is not happy."

    def display_pet(self):
        print("This dog's name is", self.petname, self.dogmood)


cat = Cat()
cat.set_petname("Fuzzy")
cat.mood("True")
cat.display_pet()

dog = Dog()
dog.set_petname("Eeyore")
dog.mood("False")
dog.display_pet()
