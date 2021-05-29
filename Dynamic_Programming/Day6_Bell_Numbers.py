'''
Bell Numbers (Number of ways to Partition a Set)
Difficulty Level : Medium
Last Updated : 16 Apr, 2021
Given a set of n elements, find number of ways of partitioning it. 
Examples: 
 

Input:  n = 2
Output: Number of ways = 2
Explanation: Let the set be {1, 2}
            { {1}, {2} } 
            { {1, 2} }

Input:  n = 3
Output: Number of ways = 5
Explanation: Let the set be {1, 2, 3}
             { {1}, {2}, {3} }
             { {1}, {2, 3} }
             { {2}, {1, 3} }
             { {3}, {1, 2} }
             { {1, 2, 3} }. 
'''
def bellNumber(n):
 
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    for i in range(1, n+1):
 
        # Explicitly fill for j = 0
        bell[i][0] = bell[i-1][i-1]
 
        # Fill for remaining values of j
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
 
    return bell[n][0]
 
# Driver program
for n in range(6):
    print('Bell Number', n, 'is', bellNumber(n))
    
#   Output  
#  Bell Number 0 is 1
# Bell Number 1 is 1
# Bell Number 2 is 2
# Bell Number 3 is 5
# Bell Number 4 is 15
# Bell Number 5 is 52
