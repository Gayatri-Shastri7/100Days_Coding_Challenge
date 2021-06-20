# Infix To Postfix
# While us humans can understand how to calculate a simple mathematical expression like 2 + 3 * 7 - 9 / 5, computers use a special technique to make it easier for them. They convert an infix expression to a postfix expression.

# An infix expression is one in which all the operators (+,-,*,/) appear between operands, just like our usual expressions.

# A postifx expression is one in which all the operands appear first, and the operators appear after the operands.

# Write a class Fixes that has 2 strings infix and postfix. It should have a parameterized constructor to accept the value of infix.

# Also, it should have a method called convert that converts the infix to a postfix expression and stores it in the postfix.

# Write only the Fixes class. Main class has already been written.

# Hint: Check google for tutorials on infix to postfix conversion first. Then write the code for it.
# Note: all operands will be of single digit only

# Example Input:
# 2+3*7-9/5
# Output:
# 237*+95/-
# Example Input:
# (2+3)*7-9/2^1
# Output:
# 23+7*921^/-

class Fixes:
    def __init__(self,infix):
        self.infix=infix
        self.postfix=[]
        self.data = []
        self.top = -1
    def push(self, element):
        self.data.append(element)
        self.top = self.top + 1
    def pop(self):
        popped_element = None
        if(self.top>-1):
            popped_element = self.data.pop()
            self.top = self.top - 1
        return popped_element
    def isEmpty(self):
        if len(self.data) == 0:
            return 1
        return 0
    def precedence(self,i):
        if(i=='^'):
            return 4
        elif(i=='*' or i=='/' or i=='%'):
            return 3
        elif(i=='+' or i=='-'):
            return 2
        elif(i=='(' or i==')'):
            return 1
        else:
            return 0
    def isoperator(self,i):
        if(i=='+' or i=='-' or i=='*' or i=='/' or i=='%' or i=='^'):
            return 1
        else:
            return 0
    def convert(self):
        for i in self.infix:
            if(self.precedence(i)==0):
                self.postfix.append(i)
            elif(i==')'):
                while(self.data[self.top]!='('):
                    self.postfix.append(self.pop())
                self.pop()
            elif(i=='('):
                self.push(i)
            elif(self.isoperator(i)):
                if(self.top==0 and self.data[0]=='('):
                    if(self.precedence(i)>self.precedence(self.data[-1])):
                        self.push(i)
                else:
                    while(self.top!=-1):
                        if(self.precedence(i)<=self.precedence(self.data[-1])):
                            self.postfix.append(self.pop())
                        else:
                            break
                    self.push(i)
        while(not(self.isEmpty())):
            self.postfix.append(self.pop())
        str1=''
        for i in self.postfix:
            if(i!='\r'):
                str1=str1+i
        self.postfix=str1


## write Fixes class above this line ##

testcases = int(input())
for _ in range(testcases):
    equation = input()
    fix = Fixes(equation)
    print(f'Infix: {equation}')
    fix.convert()
    print(f'Postfix: {fix.postfix}')
    print('---')

#     Status
# Test Cases Passed
# Input
# 3
# 2+3*7-9/5
# (2+3)*7-9/2^1
# 3*3-7/8+1/4-8-6/9+1
# Expected Output
# Infix: 2+3*7-9/5
# Postfix: 237*+95/-
# ---
# Infix: (2+3)*7-9/2^1
# Postfix: 23+7*921^/-
# ---
# Infix: 3*3-7/8+1/4-8-6/9+1
# Postfix: 33*78/-14/+8-69/-1+
# ---
# Your Output
# Infix: 2+3*7-9/5
# Postfix: 237*+95/-
# ---
# Infix: (2+3)*7-9/2^1
# Postfix: 23+7*921^/-
# ---
# Infix: 3*3-7/8+1/4-8-6/9+1
# Postfix: 33*78/-14/+8-69/-1+
# ---
