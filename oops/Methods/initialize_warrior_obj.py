# Initialize Warrior object
# Write a class called Warrior  

# The __init__ method should initialize the properties name and attack. name is a string; attack is a boolean value which says if current object is attacking or not

class Warrior:
    def __init__(self,name,attack):
        self.name= name
        self.attack = attack
        







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

'''
Status
Test Cases Passed
Input
Jack
True
Expected Output
warrior1's name is Jack. Is attacking? True
Your Output
warrior1's name is Jack. Is attacking? True
'''