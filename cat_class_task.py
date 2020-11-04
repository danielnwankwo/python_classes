# Create a class
# one function that returns "meow"

# create a 2 class level  variable
# create 3 objects
# display all info with each object
# change the class variable values in each object and display
# pseudo code each block of code

# create a class for cat
class Cat:
# define the characteristics
    animal_kingdom = "feline"

    def sound(self):
        return("meowww")

# create object(s)
# execute class functionalities with print
tabbie = Cat()

print(tabbie.animal_kingdom)
print(tabbie.sound())

alex = Cat()
print(alex.animal_kingdom)
print(alex.sound())

rowan = Cat()
print(rowan.sound())
print(rowan.animal_kingdom)

# change values of each object and display`


tabbie.animal_kingdom = "house cat"
tabbie.sound = "purr"
print(tabbie.animal_kingdom)
print(tabbie.sound())

alex.animal_kingdom = "stray"
alex.sound = "roar"
print(alex.animal_kingdom)
print(alex.sound())

rowan.animal_kingdom = "Sphinx"
rowan.sound = "hiss"
print(rowan.sound())
print(rowan.animal_kingdom)

