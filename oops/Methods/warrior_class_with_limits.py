# Warrior class, with limits
# Write a class called Warrior  

# it must have a class variable called LEVEL, initialized to 1
# The __init__ method should initialize the properties name and strength. name is a string; strength is an integer
# When initializing strength we check for LEVEL. strength will be the minimum of the 2 values: the user passed value for strength and the allowedStrength for the LEVEL
# Refer below for the values of allowedStrength:

# LEVEL	allowedStrength
# 1	20
# 2	30
# 3	50
class Warrior:
    LEVEL=1
    def __init__(self,name,strength):
        self.name=name
        if(Warrior.LEVEL==1):
            Warrior.allowedStrength=20
        elif(Warrior.LEVEL==2):
            Warrior.allowedStrength=30
        elif(Warrior.LEVEL==3):
            Warrior.allowedStrength=50
        if(strength>Warrior.allowedStrength):
            strength=Warrior.allowedStrength
        self.strength=strength


## your code above this line ##


Warrior.LEVEL = int(input())
name = input()
strength = int(input())

warrior1 = Warrior(name, strength)

print(f"Current level is {Warrior.LEVEL}")
print(f"warrior1's name is {warrior1.name}. Strength is {warrior1.strength}")
print("----")
'''
Status
Test Cases Passed
Input
2
Ares
25
Expected Output
Current level is 2
warrior1's name is Ares. Strength is 25
----
Your Output
Current level is 2
warrior1's name is Ares. Strength is 25
----
'''