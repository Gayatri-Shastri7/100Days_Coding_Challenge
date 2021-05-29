'''
Friends Pairing Problem
Difficulty Level : Medium

Given n friends, each one can remain single or can be paired up with some other friend. Each friend can be paired only once. Find out the total number of ways in which friends can remain single or can be paired up. 
 

Examples: 

Input  : n = 3
Output : 4
Explanation:
{1}, {2}, {3} : all single
{1}, {2, 3} : 2 and 3 paired but 1 is single.
{1, 2}, {3} : 1 and 2 are paired but 3 is single.
{1, 3}, {2} : 1 and 3 are paired but 2 is single.
Note that {1, 2} and {2, 1} are considered same.

'''
# Python program solution of
# friends pairing problem
 
# Returns count of ways
# n people can remain
# single or paired up.
def countFriendsPairings(n):
 
    dp = [0 for i in range(n + 1)]
 
    # Filling dp[] in bottom-up manner using
    # recursive formula explained above.
    for i in range(n + 1):
 
        if(i <= 2):
            dp[i] = i
        else:
            dp[i] = dp[i - 1] + (i - 1) * dp[i - 2]
 
    return dp[n]
 
# Driver code
n = 4
print(countFriendsPairings(n))

#Output : 10
