# Classes, Objects and Instantiation

# How to create class
# Syntax: class name_of_class starting with capital letter
# good naming convetion is required

# Classes are a way to bring data and functionlity together

class Dog:
    # defining class as variable
    animal_kind = "canine"

    # self refers to current class
    def bark(self):
        return("woof")


# in order to execute a class we have to create an object of the class
# create an object of the dog class
# functionality of dog is now located in fido
fido = Dog()

# can now put fido.whatever to execute
print(fido.animal_kind)
print(fido.bark())

# changes to one object will not have an effect on another object unless you make the change in the overall class
fido.animal_kind = "big dog"
print(fido.animal_kind)


# new object with the same functionality
lassie = Dog()
print(lassie.animal_kind)
print(lassie.bark())



