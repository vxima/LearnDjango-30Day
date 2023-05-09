## Hello World

print("Hello World!")

## Variables 

myInt = 10
myFloat = 7.0
myString = "Hello"
a , b = 3 , 4 

## Lists

myList = []
myList.append(myInt)
myList.append(myFloat)
myList.append(myString)

for x in myList: ## iterate over list 
    print(x)

## Operators

number = 1 + 2*3 - 4 ## Arithmetic
squared = 2**2
cubic = 2**3
phrase = "Hello" + " " + "World" ## Concat
mergeList = myList + [2 , 3]

## String Format

print("%s World"  , myString)
print("It's been %d years" , myInt)

## String Operations

astring = "I am Victor Ximenes"
print(astring.index("o")) ## returns index 9
print(astring.count("e")) ## returns count of "e" (2)
print(astring[1:4]) ## slice the string returning "am"
print(astring[::-1]) ## reverse string
print(astring.lower()) ## Uppercase
afewwords = astring.split(" ") ## returns a list with the every word in the string

## Conditions

t = True
f = False
print(t and f) ## False
print(t or f) ## True

if myInt > 9:
    print("Greater")

if myInt in myList:
    print("In")

nulo = None
if nulo is None:
    print("Null")

print(not False) ## True

## Loops

for i in range(5):
    print(i) # 0 ,1 , 2, ,3, 4
xi = 3
while xi>=0:
    xi -= 1
    print(xi)

##Functions

def sum_two_numbers(a, b):
    return a + b


##Classes and Objects   

class myClass:
    def __init__(self, name):
        self.name = name
    def printName(self):
        print(self.name)

myObj = myClass("Victor")
myObj.printName()

## Dictionary

dic = {
    "name" : "victor" ,
    "age" : 23
}

## Modules and packages
import numpy as np










