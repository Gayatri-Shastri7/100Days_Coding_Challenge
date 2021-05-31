# Choice of Area
# Difficulty Level : Medium
# Last Updated : 05 Feb, 2018
# Consider a game, in which you have two types of powers, A and B and there are 3 types of Areas X, Y and Z. Every second you have to switch between these areas, each area has specific properties by which your power A and power B increase or decrease. We need to keep choosing areas in such a way that our survival time is maximized. Survival time ends when any of the powers, A or B reaches less than 0.
# Examples:

# Initial value of Power A = 20        
# Initial value of Power B = 8

# Area X (3, 2) : If you step into Area X, 
#                 A increases by 3, 
#                 B increases by 2

# Area Y (-5, -10) : If you step into Area Y, 
#                    A decreases by 5, 
#                    B decreases by 10

# Area Z (-20, 5) : If you step into Area Z, 
#                   A decreases by 20, 
#                   B increases by 5

# It is possible to choose any area in our first step.
# We can survive at max 5 unit of time by following 
# these choice of areas :
# X -> Z -> X -> Y -> X

# Python code to get maximum survival time

# Class to represent an area
class area:
	def __init__(self, a, b):
		self.a = a
		self.b = b

# Utility method to get maximum survival time
def maxSurvival(A, B, X, Y, Z, last, memo):
	# if any of A or B is less than 0, return 0
	if (A <= 0 or B <= 0):
		return 0
	cur = area(A, B)

	# if already calculated, return calculated value
	for ele in memo.keys():
		if (cur.a == ele.a and cur.b == ele.b):
			return memo[ele]

	# step to areas on basis of last chosen area
	if (last == 1):
		temp = 1 + max(maxSurvival(A + Y.a, B + Y.b,
								X, Y, Z, 2, memo),
					maxSurvival(A + Z.a, B + Z.b,
								X, Y, Z, 3, memo))
	elif (last == 2):
		temp = 1 + max(maxSurvival(A + X.a, B + X.b,
								X, Y, Z, 1, memo),
			maxSurvival(A + Z.a, B + Z.b,
				X, Y, Z, 3, memo))
	elif (last == 3):
		temp = 1 + max(maxSurvival(A + X.a, B + X.b,
				X, Y, Z, 1, memo),
			maxSurvival(A + Y.a, B + Y.b,
				X, Y, Z, 2, memo))

	# store the result into map
	memo[cur] = temp

	return temp

# method returns maximum survival time
def getMaxSurvivalTime(A, B, X, Y, Z):
	if (A <= 0 or B <= 0):
		return 0
	memo = dict()

	# At first, we can step into any of the area
	return max(maxSurvival(A + X.a, B + X.b, X, Y, Z, 1, memo),
		maxSurvival(A + Y.a, B + Y.b, X, Y, Z, 2, memo),
		maxSurvival(A + Z.a, B + Z.b, X, Y, Z, 3, memo))

# Driver code to test above method
X = area(3, 2)
Y = area(-5, -10)
Z = area(-20, 5)

A = 20
B = 8
print(getMaxSurvivalTime(A, B, X, Y, Z))

# Output:
# 5


