# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

class MyClass:  # create class
    x = 5  # create proprty x

p2 = MyClass()

p2.x=4 #modify object
#del p1.age #delete object prop
#del p2 #delete oibject
print(p2.x)

class MyClass2:

    def __init__(self, name, age):  # The __init__() Function
        self.name = name
        self.age = age

    def myfunc(self):  # Object Methods
        print("Hello my name is " + self.name)


p1 = MyClass2("John", 36)
p1.myfunc()


# print(p1.name)
# print(p1.age)


# note: in python declare method in class is different so be carefull here
