# Jared Godfrey
# CIS129
# 5-13-24
# Module 12 Lab
"""Defining a pet class function"""

def main():

    #declare Input Variables
    inputName = ''
    inputType = ''
    inputAge = 0

    #class variable to hold a pet
    Animal = None

    #create a pet object
    Animal = Pet(inputName, inputType, inputAge)

    #Get variables to hold a pet
    inputName = input('Enter a pet name: ')
    Animal.setName(inputName)

    inputType = input('Enter a pet type: ')
    Animal.setType(inputType)

    inputAge = input('Enter a pet age: ')
    Animal.setAge(inputAge)

    #Show values for this pet
    print('The pet name is ' + Animal.getName())
    print('The pet type is ' + Animal.getType())
    print('The pet age is ' + Animal.getAge())

#declare pet class
class Pet():
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

    # Constructor
    def Pet(self, n, t, a):
        Pet.name = n
        Pet.type = t
        Pet.age = a

    # Mutators
    def setName(self, n):
        self.name = n

    def setType(self, t):
        self.type = t

    def setAge(self, a):
        self.age = a

    # Accessors
    def getName(self):
        name = self.name
        return name
    
    def getType(self):
        type = self.type
        return type
    
    def getAge(self):
        age = self.age
        return age

main()
