# Change Warrior Name
# Write a class called Warrior  

# The __init__ method should initialize the properties name and attack. name is a string; attack is a boolean value which says if current object is attacking or not
# Also write a method called updateName . This toggles the case for each character in the name string of the given Warrior object and updates the name. eg, if warrior1.name is Apollo then warrior1.updateName() will make warrior1.name as aPOLLO
# Write only the Warrior class. The rest of the code has been written. Check the remaining code to understand how the input is being taken.
class Warrior:
    def __init__(self,name,attack):
        self.name = name
        self.attack = attack
        
    def updateName(self):
        self.name = self.name.swapcase()
        return(self.name)










## your code above this line ##

def bool_convert(line):
    if(line == "True"):
        line = True
    else:
        line = False
    return line

name = input()
attack = bool_convert(input())

warrior1 = Warrior(name, attack)

print(f"warrior1's name is {warrior1.name}. Is attacking? {warrior1.attack}")

warrior1.updateName()

print(f"warrior1's name is {warrior1.name}. Is attacking? {warrior1.attack}")

warrior1.updateName()

print(f"warrior1's name is {warrior1.name}. Is attacking? {warrior1.attack}")
'''
Test Cases Passed
Input
Apollo
True
Expected Output
warrior1's name is Apollo. Is attacking? True
warrior1's name is aPOLLO. Is attacking? True
warrior1's name is Apollo. Is attacking? True
Your Output
warrior1's name is Apollo. Is attacking? True
warrior1's name is aPOLLO. Is attacking? True
warrior1's name is Apollo. Is attacking? True
'''