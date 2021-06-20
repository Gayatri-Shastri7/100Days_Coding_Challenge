### write your solution below this line ### 
# Implement Stack and its operations
# Write a program to implement the following operations in a Stack:

# Operations:

# push:       To add the elements into Stack
# pop:         To remove the element from Stack and return the element.
# peek:        To get the top element from the Stack and return the element.
# isEmpty:   returns 1 is stack is empty. Else returns 0
# isFull:       returns 1 is stack is full. Else returns 0
# Some code has already been written. Please use the given structure / class to write your own functions


# output:
#  Status
# Test Cases Passed
# Input
# 10
# 10
# 5
# 4
# 1 1
# 1 1
# 1 2
# 1 3
# 1 4
# 3
# 2
# 3
# Expected Output
# isFull:0
# isEmpty:1
# push:1
# push:1
# push:2
# push:3
# push:4
# peek:4
# pop:4
# peek:3
# Your Output
# isFull:0
# isEmpty:1
# push:1
# push:1
# push:2
# push:3
# push:4
# peek:4
# pop:4
# peek:3

class Stack:
 
    # Constructor to initialize the stack
    def __init__(self, size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1
 
    # Function to add an element `x` to the stack
    def push(self, x):
        if self.isFull():
            exit(1)
        self.top = self.top + 1
        self.arr[self.top] = x
 
    # Function to pop a top element from the stack
    def pop(self):
        # check for stack underflow
        if self.isEmpty():
            exit(1)
        # decrease stack size by 1 and (optionally) return the popped element
        top = self.arr[self.top]
        self.top = self.top - 1
        return top
 
    # Function to return the top element of the stack
    def peek(self):
        if self.isEmpty():
            exit(1)
        return self.arr[self.top]
 
    # Function to return the size of the stack
    def size(self):
        return self.top + 1
 
    # Function to check if the stack is empty or not
    def isEmpty(self):
        if self.size() == 0:
            return 1
        else:
            return 0
 
    # Function to check if the stack is full or not
    def isFull(self):
        if self.size() == self.capacity:
            return 1
        else:
            return 0
 





if __name__ == "__main__": 
    
    test_cases=int(input()) # number of test cases
    size=int(input()) # size of Stack
    stack=Stack(size) # creating new stack object
    
    while(test_cases>0): 
        instruction=input().split()
        val=0
        if len(instruction)>1:
            val=int(instruction[1])

        instruction=int(instruction[0])
        #####
        # Instruction 1 means Push
        # Instruction 2 means Pop
        # Instruction 3 means Peek
        # Instruction 4 means isEmpty
        # Instruction 5 means isFull
        #####

        if(instruction==1):  
            print(f'push:{val}')
            stack.push(val)

        elif (instruction==2):
            print(f'pop:{stack.pop()}')

        elif (instruction==3):            
            print(f'peek:{stack.peek()}')

        elif(instruction==4):
            print(f'isEmpty:{stack.isEmpty()}')

        elif(instruction==5):
            print(f'isFull:{stack.isFull()}')

        test_cases=test_cases-1 
