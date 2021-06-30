# Initialize Warrior object with varying damage
# Write a class called Warrior  

# The __init__ method should initialize the properties name ,attack and strength.
# name is a string; attack is a boolean value which says if current object is attacking or not.
# strength is an integer
# Additionally it should have a method called damage. The damage method returns the amount of damage done by the given Warrior object. Use the table below to determine the amount of damage done
# attack	strength	damage
# False	any value	0
# True	0	0
# True	1 to 10 (both inclusive)	20
# True	11 to 20 (both inclusive)	30
# True	Greater than 20	100
# Write only the Warrior class. The rest of the code has been written. Check the remaining code to understand how the input is being taken.

class Warrior:
    def __init__(self,name,attack,strength):
        self.name=name
        self.attack=attack
        self.strength=strength
    def damage(self):
        if self.attack == False:
            return (0)
        else:
            if self.strength == 0:
                return(0)
            elif(self.strength>=1 and self.strength<=10):
                return 20
            elif(self.strength>=11 and self.strength<=20):
                return 30
            elif(self.strength>20):
                return 100





## your code above this line ##

def bool_convert(line):
    if(line == "True"):
        line = True
    else:
        line = False
    return line


name = input()
attack = bool_convert(input())
strength = int(input())

warrior1 = Warrior(name, attack, strength)

name = input()
attack = bool_convert(input())
strength = int(input())

warrior2 = Warrior(name, attack, strength)

print(f"warrior1's name is {warrior1.name}. Is attacking? {warrior1.attack}")
print(f"warrior1's damage is {warrior1.damage()}")
print("----")

print(f"warrior2's name is {warrior2.name}. Is attacking? {warrior2.attack}")
print(f"warrior2's damage is {warrior2.damage()}")
print("----")

'''
Test Cases Passed
Input
Jack
True
10
Jim
False
10
Expected Output
warrior1's name is Jack. Is attacking? True
warrior1's damage is 20
----
warrior2's name is Jim. Is attacking? False
warrior2's damage is 0
----
Your Output
warrior1's name is Jack. Is attacking? True
warrior1's damage is 20
----
warrior2's name is Jim. Is attacking? False
warrior2's damage is 0
----
'''