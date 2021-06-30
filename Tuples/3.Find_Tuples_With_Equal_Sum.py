'''
Find Tuples with Equal Sums
Complete the given method called solve which takes as parameter a list of tuples called A.

You have to print that pair of tuple which have the same sum. There is only 1 such pair.

Example:

[(1,2), (1,0), (4,4), (10,2), (5,-1), (1,1,1)]

For this list, the pair is:

1,2
1,1,1
Because both these tuples sum up to 3.
'''
def solve(A):
    # write your code here
    l1=[]
    for i in range(len(A)):
        sum1=0
        for j in A[i]:
            sum1=sum1+j
            a=A[i]
        for k in range(i+1,len(A)):
            sum2=0
            for m in A[k]:
                sum2=sum2+m
            if(sum1==sum2):
                l1.append(a)
                l1.append(A[k])
    for i in l1:
        for j in i:
            print(j,end=" ")
        print()                                                                     
'''
Status
Test Cases Passed
Expected Output
Input: [(1, 2), (1, 0), (4, 4), (10, 2), (5, -1), (1, 1, 1)]
Output:
1 2 
1 1 1 
Your Output
Input: [(1, 2), (1, 0), (4, 4), (10, 2), (5, -1), (1, 1, 1)]
Output:
1 2 
1 1 1 
'''                            