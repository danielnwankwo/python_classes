# This will cover classes in python
## OOP OBJECT ORIENTED PROGRAMMING
### Four Pillars

- Inheritance - this is the most utilised
 
- Encapsulation -  you can restrict access to methods and attributes of a certain class. This prevents accidental modification of data and unwanted changes

- Abstraction - 

- Polymorphism - objects of a particular class can be used as if it belonged to a different class.

- What are Classes 
- Why
- Class is the main factor that is used to implement any of these pillars

# Classes, Objects and Instantiation

# How to create class
# Syntax: class name_of_class starting with capital letter
# good naming convention is required

# Classes are a way to bring data and functionality together`

# first define the class

```
class Dog:
    # defining class as variable
    animal_kind = "canine" 
```

# self refers to current class
# define the attributes as a function

    def bark(self):
        return("woof")


# in order to execute a class we have to create an object of the class
# create an object of the dog class
# functionality of dog is now located in fido



 ``` fido = Dog() ```




# can now put fido.whatever to execute

```
print(fido.animal_kind)
print(fido.bark())
```




# new object with the same functionality



 ```
lassie = Dog()
print(lassie.animal_kind)
print(lassie.bark())
```






# changes to one object will not have an effect on another object unless you make the change in the overall class



```
fido.animal_kind = "big dog"
print(fido.animal_kind)
```


 


