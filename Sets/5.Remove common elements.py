'''
Remove common elements
Complete the given method called solve which takes as parameter a list A and B.

You have to return a list which does not contain the elements that occur in both the lists. Your returned list should be in sorted order

Example Input:
1 2 5 7 8
7 0 10 2 15
 
Output:
0 1 5 8 10 15
Here, 2 and 7 occur in both lists and hence have been eliminated from the final list.
'''
def solve(A,B):
    
    return(sorted(list(set(A)^set(B))))

'''
Status
Test Cases Passed
Expected Output
Input:
[1, 2, 5, 7, 8]
[7, 0, 10, 2, 15]
Output:
0 1 5 8 10 15 
Your Output
Input:
[1, 2, 5, 7, 8]
[7, 0, 10, 2, 15]
Output:
0 1 5 8 10 15 
'''