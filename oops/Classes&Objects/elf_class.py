'''
The Elf Class
Define the Elf class with the following methods, that will be called by it's objects:

say_hello - prints the message Howdy, elf here!
magic - accepts as parameter a number n, and returns the factorial of the number n
Write only the Elf class. The remaining code has already been written
'''
class Elf:
    def say_hello(self):
        print('Howdy, elf here!')
    def magic(self,n):
        
        fact =1
        for i in range(1,n+1):
            fact = fact * i
        return(fact)





## your code above this line ##

elf1 = Elf()

elf1.say_hello()

n = int(input())

magical_number  = elf1.magic(n)
print("Magical number is", magical_number)
'''
Status
Test Cases Passed
Input
5
Expected Output
Howdy, elf here!
Magical number is 120
Your Output
Howdy, elf here!
Magical number is 120
'''
