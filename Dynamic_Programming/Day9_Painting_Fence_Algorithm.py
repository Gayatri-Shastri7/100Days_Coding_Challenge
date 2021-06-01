# Given a fence with n posts and k colors, find out the number of ways of painting the fence such that at most 2 adjacent posts have the same color. Since answer can be large return it modulo 10^9 + 7.
# Examples:

# Input : n = 2 k = 4
# Output : 16
# We have 4 colors and 2 posts.
# Ways when both posts have same color : 4 
# Ways when both posts have diff color :
# 4(choices for 1st post) * 3(choices for 
# 2nd post) = 12

# Input : n = 3 k = 2
# Output : 6

# Python3 program for Painting Fence Algorithm
# optimised version
 
# Returns count of ways to color k posts
def countWays(n, k):
     
    dp = [0] * (n + 1)
    total = k
    mod = 1000000007
     
    dp[1] = k
    dp[2] = k * k   
     
    for i in range(3,n+1):
        dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod
         
    return dp[n]
   
# Driver code
n = 3
k = 2
print(countWays(n, k))
