# Write a class called Warrior  

# The __init__ method should initialize the properties name and attack. name is a string; attack is a boolean value which says if current object is attacking or not
# Also write a method called myEnemy. This method accepts as parameter an object of Boy class. (You can refer to the Boy class given below.) The method outputs the following: My name is [Warrior Name] and my enemy is [Boy Name] where Warrior Name and Boy Name are names of the Warrior and Boy object, respectively

class Warrior:
    def __init__(self,name,attack):
        self.name=name
        self.attack=attack
    def myEnemy(self,boy):
        self.boy=boy
        print(f"My name is [{self.name}] and my enemy is [{self.boy.name}]")


## your code above this line ##

class Boy:
    def __init__(self,name):
        self.name = name

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

boy_name = input()
boy1 = Boy(boy_name)

warrior1.myEnemy(boy1)

'''
est Cases Passed
Input
Appollo
True
Jack
Expected Output
warrior1's name is Appollo. Is attacking? True
My name is [Appollo] and my enemy is [Jack]
Your Output
warrior1's name is Appollo. Is attacking? True
My name is [Appollo] and my enemy is [Jack]
'''