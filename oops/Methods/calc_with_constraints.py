# Calculator, with constants
# Let's revisit our Calculator class. Apart from simple mathematical formulas, we will need to calculate some complex formulas too.

# Write a Calculator class that has the following class variables

# variable	value
# g	9.8
# e	2.71
# pi	3.14
# Additionally, each object should have the following methods:

# add - accepts as parameters 2 numbers and returns the sum of the 2 numbers
# absolute - accepts as parameters 2 numbers and returns the absolute difference of the 2 numbers
class Calculator:
    '''
    def __init__(self,a=None,b=None):
        self.a =a
        self.b =b
    '''
    g= 9.8
    e= 2.71
    pi= 3.14
    def add(self,a,b):
        return(a + b)
    def absolute(self,a,b):
        return(abs(a - b))








a = int(input())
b = int(input())

calc = Calculator()

if(a > b):
    print(f"{a} added to g = {calc.add(a,Calculator.g)}")
else:
    print(f"absolute of {b} and e = {calc.absolute(b,Calculator.e)}")

Calculator.pi = 2.14

print(f"Now pi is {Calculator.pi}")

'''
Status
Test Cases Passed
Input
2
3
Expected Output
absolute of 3 and e = 0.29000000000000004
Now pi is 2.14
Your Output
absolute of 3 and e = 0.29000000000000004
Now pi is 2.14
'''
