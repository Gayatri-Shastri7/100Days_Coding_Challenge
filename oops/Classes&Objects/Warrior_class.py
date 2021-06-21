'''
The Warrior Class
Define the Warrior class with the following methods, that will be called by it's objects:

say_hello - prints the message Argh! I am a Warrior!
roar - accepts as parameter a number, and prints a roar that many times.
Example: warrior1.roar(5) prints RoarRoarRoarRoarRoar where warrior1 is an object of type Warrior
Write only the Warrior class. The remaining code has already been written.
'''
class Warrior:
    def say_hello(self):
        print("Argh! I am a Warrior!")
    def roar(self,times):
        print(times*"Roar")









## your code above this line ##

warrior1 = Warrior()

warrior1.say_hello()

times = int(input())

warrior1.roar(times)
'''
Status
Test Cases Passed
Input
5
Expected Output
Argh! I am a Warrior!
RoarRoarRoarRoarRoar
Your Output
Argh! I am a Warrior!
RoarRoarRoarRoarRoar
'''
