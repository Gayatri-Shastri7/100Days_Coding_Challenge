'''
Find tuples with same starting and ending alphabets
Complete the given method called solve which takes as parameter a list of tuples called A.

Each tuple contains some strings. You have to print the indexes of those tuples whose first element's first alphabet is the same as the last element's last alphabet.

Example, for this list:

[('hello','hi'), ('his', 'name', 'archith'), ('kremlin', 'russia', 'spartak'), ('error', 'none', 'wave'), ('indeed', 'numbers', 'work')]
The output is:

1 2 3

Because tuples in index 1 2 and 3 obey the given condition.
'''
def solve(A):
    # write your code here
    for i in A:
        l1=i[0]
        l2=i[-1]
        if(l1[0] is l2[-1]):
            print(A.index(i),end=' ')

'''
Status
Test Cases Passed
Expected Output
Input: [('hello', 'hi'), ('his', 'name', 'archith'), ('kremlin', 'russia', 'spartak'), ('error', 'none', 'wave'), ('indeed', 'numbers', 'work')]
Output:
1 2 3 
Your Output
Input: [('hello', 'hi'), ('his', 'name', 'archith'), ('kremlin', 'russia', 'spartak'), ('error', 'none', 'wave'), ('indeed', 'numbers', 'work')]
Output:
1 2 3 
'''