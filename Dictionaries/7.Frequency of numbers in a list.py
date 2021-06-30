'''
Frequency of numbers in a list
Given a list of integers, find the frequency of each integer in the list.

Complete the given method called solve which takes as parameter a list of integers called items, Print the frequency of Integers in sorted by keys.

Example Input:
1, 7, 9, 100, 3, 8, 2, 50, 21, 9 , 200, 1, 200, 200, 200
 
Output:
1 : 2
2 : 1
3 : 1
7 : 1
8 : 1
9 : 2
21 : 1
50 : 1
100 : 1
200 : 4
'''
def solve(items):
    # write a code from here
    all_freq = {}
    for i in items:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    for i in sorted (all_freq) :
        print (str(i)+':',all_freq[i])
'''
Status
Test Cases Passed
Expected Output
Input:
1 7 9 100 3 8 2 50 21 9 200 1 200 200 200 
Output:
1: 2
2: 1
3: 1
7: 1
8: 1
9: 2
21: 1
50: 1
100: 1
200: 4
Your Output
Input:
1 7 9 100 3 8 2 50 21 9 200 1 200 200 200 
Output:
1: 2
2: 1
3: 1
7: 1
8: 1
9: 2
21: 1
50: 1
100: 1
200: 4
'''