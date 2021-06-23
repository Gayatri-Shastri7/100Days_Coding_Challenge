'''
Slice a Tuple
Complete the given method called solve which takes as parameter a tuple A.

You have to return a new tuple with the first element and last 2 elements removed. A is guaranteed to be of at least 4 elements.

Example Input:
1 3 5 7

Output:
3
'''
def solve(A):
    # write your code from here
    slice= A[1:-2]
    return((slice))

'''
Status
Test Cases Passed
Expected Output
Input: (1, 3, 5, 7)
Output: 3 
Your Output
Input: (1, 3, 5, 7)
Output: 3 
'''