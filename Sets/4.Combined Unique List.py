'''
Combined Unique List
Complete the given method called solve which takes as parameter a list A and B.

You have to print only the unique elements of the lists if both of them are combined, in sorted order.

Example Input:
1 2 5 7 8
7 0 10 2 15
 
Output:
0 1 2 5 7 8 10 15
'''
def solve(A,B):
    # write your code from here
    for i in B:
        A.append(i)
    print(*sorted(set(A)))

'''
Status
Test Cases Passed
Expected Output
Input:
[1, 2, 5, 7, 8]
[7, 0, 10, 2, 15]
Output:
0 1 2 5 7 8 10 15 
Your Output
Input:
[1, 2, 5, 7, 8]
[7, 0, 10, 2, 15]
Output:
0 1 2 5 7 8 10 15
'''