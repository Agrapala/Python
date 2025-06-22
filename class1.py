# This code defines a class `Phone` with a method `say` that prints a greeting message.
class Phone :
    def say(self,name):
        self.x = name
        print("Hello, I am " + name)


samsung = Phone()
samsung.say("Samsung")
print(samsung.x)
samsung.x = "Samsung Galaxy"
print(samsung.x)

#New class 

class student:
    name = "Samitha"
    age = 23

student1 = student()
print(student1.name)
print(student1.age)

#class with --init--
class car:
    def __init__(self,name,year):
        self.name = name
        self.year = year

car1 = car("BMW", 2023)
print(car1.name)
print(car1.year)
car2 = car("Audi", 2024)
print(car2.name)
print(car2.year)

#Encapsulation
class Person:
    x = 10
    _y = 20; 

man1 = Person()
print(man1._y)

class encaap1:
    def meth1(self):
        print("welcome srilanka")
        self.__meth2()
    def __meth2(self):
        print("Welcome sinhalee's country")

enca = encaap1()
enca.meth1()

## inheritance
class inhe1:
    def meth1(self):
        print("This is parent class")
class inhe2(inhe1):
    def meth2(self):
        print("This is child class")

inhe = inhe2()
inhe.meth1()
inhe.meth2()
