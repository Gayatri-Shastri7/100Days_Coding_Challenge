'''
Dictionary Distance
Complete the given method called solve which takes as parameter 2 dictionaries A and B.

A contains the x,y coordinates for the first point and B the x,y, coordinates of the second point. You have to find out the distance between these 2 points and print it.

Example Input:
{'x': 4, 'y': 7}
{'x': 1, 'y': 3}
 
Output:
5
'''
#Method-1
def solve(A,B):
    # write your logic from here
    a = (A['x'] - B['x']) ** 2
    b = (A['y'] - B['y']) ** 2
    print(int((a+b)**0.5))
    
#Method-2
def solve(A,B):
    # write your logic from here
    a= (A['x']-B['x'])
    b =(A['y']-B['y'])
    print(int((a*a+b*b)**0.5))
'''
Status
Test Cases Passed
Expected Output
Input: 
A
{'x': 4, 'y': 7}
B
{'x': 1, 'y': 3}
Output:
5
Your Output
Input: 
A
{'x': 4, 'y': 7}
B
{'x': 1, 'y': 3}
Output:
5
'''
