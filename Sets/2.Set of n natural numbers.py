'''
Set of n natural numbers
Complete the given method called solve which takes as parameter an integer n

You have to generate and return a set with the first n natural numbers

Example Input: 4

Output:

{1, 2, 3, 4}
'''

def solve(n):
    # write your code from here
    k={}
    s=set(k)
    for i in range(1,n+1):
        s.add(i)
    return s
'''
Status
Test Cases Passed
Expected Output
Input: 4
1 2 3 4 
You have returned a :
Your Output
Input: 4
1 2 3 4 
You have returned a :
'''