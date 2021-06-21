'''
Initialize Boy object with speed
Write a class called Boy .

The __init__ method should initialize the properties clothes , mood and speed. clothes and mood are strings; speed is an integer
Objects of this class should have a method called accelerate which increases the speed of the Boy object by 10
Write only the Boy class. The rest of the code has been written. Check the remaining code to understand how the input is being taken.
'''
class Boy:
    def __init__(self,clothes,mood,speed):
        self.clothes = clothes
        self.mood = mood
        self.speed = speed
        self.acc = 10 + self.speed
    def accelerate(self):
        self.speed += 10
        return(self.speed)




## your code above this line ##

clothes = input()
mood = input()
speed = int(input())

boy1 = Boy(clothes,mood,speed)

print(f"boy1's cloths are {boy1.clothes} and mood is {boy1.mood}")
print(f"boy1's current speed is {boy1.speed}")

boy1.accelerate()
print(f"After acceleration, boy1's speed is {boy1.speed}")

'''
Status
Test Cases Passed
Input
Summer
Happy
10
Expected Output
boy1's cloths are Summer and mood is Happy
boy1's current speed is 10
After acceleration, boy1's speed is 20
Your Output
boy1's cloths are Summer and mood is Happy
boy1's current speed is 10
After acceleration, boy1's speed is 20
'''