'''
Initialize Boy object
Write a class called Boy . The __init__ method should initialize the properties clothes and mood . Both these properties are strings

Write only the Boy class. The rest of the code has been written. Check the remaining code to understand how the input is being taken.

Your Answer
'''
class Boy:
    def __init__(self,clothes,mood):
        self.clothes = clothes
        self.mood = mood







## your code above this line ##

clothes = input()
mood = input()

boy1 = Boy(clothes,mood)

print(f"boy1's cloths are {boy1.clothes} and mood is {boy1.mood}")

'''
Status
Test Cases Passed
Input
Summer
Happy
Expected Output
boy1's cloths are Summer and mood is Happy
Your Output
boy1's cloths are Summer and mood is Happy
'''