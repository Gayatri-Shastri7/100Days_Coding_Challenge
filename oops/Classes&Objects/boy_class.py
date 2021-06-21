'''
The Boy Class
Define a Boy class with the following methods, that will be called by it's objects:

say_hello - prints the message Hi! Welcome to the game!
say_time - it should accept as parameter the hour and minute and say the time, like this: It has been 7 hours and 20 minutes
Write only the Boy class. The remaining code has already been written.
'''
class Boy:
    def say_hello(self):
        print("Hi! Welcome to the game!")
    def say_time(self,hour,minute):
        print("It has been "+str(hour)+" hours and "+str(minute)+" minutes")
        
        



## your code above this line ##

boy1 = Boy()

boy1.say_hello()

hour = int(input())
minute = int(input())

boy1.say_time(hour, minute)
'''
Status
Test Cases Passed
Input
7
20
Expected Output
Hi! Welcome to the game!
It has been 7 hours and 20 minutes
Your Output
Hi! Welcome to the game!
It has been 7 hours and 20 minutes
'''
