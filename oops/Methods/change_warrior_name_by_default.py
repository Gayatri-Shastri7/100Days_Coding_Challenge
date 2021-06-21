# Change Warrior name, by default
# Write a class called Warrior  

# The __init__ method should initialize the properties name and attack. name is a string; attack is a boolean value which says if current object is attacking or not
# Also write a method called updateName .
# - By default the updateName method appends the word updated to the object's name
# - If the parameter passed is upper then the name is changed to uppercase
# - In all other cases, the name is changed to lower case
# Example, if warrior1.name is Apollo then
# warrior1.updateName() will make warrior1.name as Apolloupdated
# Example, if warrior1.name is Ares then
# warrior1.updateName("upper") will make warrior1.name as ARES
# Example, if warrior1.name is POSeIdon then
# warrior1.updateName("other") will make warrior1.name as poseidon
class Warrior:
    def __init__(self,name,attack):
        self.name=name
        self.attack=attack
    def updateName(self,change="updated"):
        if(change=="updated"):
            self.name=self.name+"updated"
        elif(change=="upper"):
            self.name=self.name.upper()
        else:
            self.name=self.name.lower()



## your code above this line ##

def bool_convert(line):
    if(line == "True"):
        line = True
    else:
        line = False
    return line

name = input()
attack = bool_convert(input())
change_to_1 = input()
change_to_2 = input()


warrior1 = Warrior(name, attack)

print(f"warrior1's name is {warrior1.name}. Is attacking? {warrior1.attack}")

warrior1.updateName()
print(f"warrior1's name is {warrior1.name}. Is attacking? {warrior1.attack}")

warrior1.updateName(change_to_1)
print(f"warrior1's name is {warrior1.name}. Is attacking? {warrior1.attack}")

warrior1.updateName(change_to_2)
print(f"warrior1's name is {warrior1.name}. Is attacking? {warrior1.attack}")

'''
Test Cases Passed
Input
Ares
True
other
upper
Expected Output
warrior1's name is Ares. Is attacking? True
warrior1's name is Aresupdated. Is attacking? True
warrior1's name is aresupdated. Is attacking? True
warrior1's name is ARESUPDATED. Is attacking? True
Your Output
warrior1's name is Ares. Is attacking? True
warrior1's name is Aresupdated. Is attacking? True
warrior1's name is aresupdated. Is attacking? True
warrior1's name is ARESUPDATED. Is attacking? True
'''