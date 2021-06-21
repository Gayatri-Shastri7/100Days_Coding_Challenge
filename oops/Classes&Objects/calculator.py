'''
Calculator Class
Let us now write our very own Calculator class.

Each object of this class should have the following methods:

sum - accepts as parameter a list of numbers and returns the sum of all the numbers
minus - accepts as parameter only two numbers: first a and then b. It must return a - b
multiply - accepts as parameter 4 numbers in the form of a list and returns the products of all 4 numbers
divide - accepts as parameter only two numbers: first a and then b. It must return a // b. If b is 0, it return Div by 0 not allowed!
Write only the Calculator class. The rest of the code has been written. Check the remaining code to understand how the input is being taken.
'''
class Calculator:
    def sum(self,sum_list):
        return(sum(sum_list))
    
    def minus(self,first,second):
        return(first-second)
        
    def multiply(self,sum_list):
        return(sum_list[0]*sum_list[1]*sum_list[2]*sum_list[3])
    
    def divide(self,first,second):
        if(second==0):
            return("Div by 0 not allowed!")
        for c in range(1,second+1):
            return(first//second)

        


## your code above this line ##

calc = Calculator()

first = int(input())
second = int(input())
third = int(input())
fourth = int(input())
fifth = int(input())

sum_list = [first,second,third,fourth,fifth]
answer_1 = calc.sum(sum_list)
print(f"Sum of {sum_list} is {answer_1}")

answer_2 = calc.minus(first,second)
print(f"{first} - {second} = {answer_2}")

answer_3 = calc.multiply(sum_list[:-1]) # selecting only first 4 values
print(f"Multiplying {sum_list[:-1]} = {answer_3}")

answer_4 = calc.divide(fourth,fifth)
print(f"Dividing {fourth}/{fifth} = {answer_4}")

'''
Status
Test Cases Passed
Input
5
4
2
3
1
Expected Output
Sum of [5, 4, 2, 3, 1] is 15
5 - 4 = 1
Multiplying [5, 4, 2, 3] = 120
Dividing 3/1 = 3
Your Output
Sum of [5, 4, 2, 3, 1] is 15
5 - 4 = 1
Multiplying [5, 4, 2, 3] = 120
Dividing 3/1 = 3
'''
