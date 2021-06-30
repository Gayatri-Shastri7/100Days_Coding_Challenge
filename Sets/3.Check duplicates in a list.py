'''
Complete the given method called solve which takes as parameter a list A.

You have to print the number of duplicate and the number of unique elements.

Example Input:
1 2 3 4 5 4 3
 
Output:
Unique: 5
Duplicate: 2
 
Example Input:
18 18 18 18 18
 
Outupt:
Unique: 1
Duplicate: 4

'''
def solve(A):
    # write your code here
    l=len(A)
    k=set(A)
    m=len(k)
    print(f"Unique: {m}")
    print(f"Duplicate: {l-m}")

'''
Status
Test Cases Passed
Expected Output
Input: [1, 2, 3, 4, 5, 4, 3]
Output:
Unique: 5
Duplicate: 2
Your Output
Input: [1, 2, 3, 4, 5, 4, 3]
Output:
Unique: 5
Duplicate: 2
'''