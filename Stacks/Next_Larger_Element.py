# Next Larger Element (A)
# Given an array, find the Next greater element for every element.

# The Next greater Element for an element x is the first greater element on the right side of x in array.

# Elements for which no greater element exist, consider next greater element as -1.

# Example :
# Input :
# A : [4, 5, 2, 25]
# Output :
#    [5, 25, 25, -1]

class Solution:
    def nextGreaterElement(self, arr):

  
        s = list()
        n = len(arr)
        arr1 = [0 for i in range(n)]

        # iterating from n-1 to 0
        for i in range(n - 1, -1, -1): 

            # We will pop till we get the greater  
            # element on top or stack gets empty
            while (len(s) > 0 and s[-1] <= arr[i]):
                s.pop()

            # if stack gots empty means there 
            # is no element on right which is 
            # greater than the current element.
            # if not empty then the next greater 
            # element is on top of stack
            if (len(s) == 0):
                arr1[i] = -1        
            else:
                arr1[i] = s[-1]     

            s.append(arr[i])

        for i in range(n):
            print(arr1[i],end=" " )

    # Driver Code
    #arr = list(map(int,input()))
        return ('')
        
# Status
# Test Cases Passed
# Expected Output
# INPUT(s):
# 4 5 2 25 

# OUTPUT(s):
# 5 25 25 -1 

# INPUT(s):
# 13 7 6 12 

# OUTPUT(s):
# -1 12 12 -1 

# INPUT(s):
# 1 2 3 4 

# OUTPUT(s):
# 2 3 4 -1 

# Your Output
# INPUT(s):
# 4 5 2 25

# OUTPUT(s):
# 5 25 25 -1 

# INPUT(s):
# 13 7 6 12

# OUTPUT(s):
# -1 12 12 -1 

# INPUT(s):
# 1 2 3 4

# OUTPUT(s):
# 2 3 4 -1 
