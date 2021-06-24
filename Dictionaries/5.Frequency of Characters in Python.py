'''
Frequency of Characters in Python
Complete the given method called solve which takes as parameter a list of strings called words.

You have to calculate the frequency of each alphabet throughout the list.

Print the frequency of each alphabet. Print the alphabets in sorted order.

Example Input:
hello these are some awesome words for edyst
 
Output:
a : 2
d : 2
e : 8
f : 1
h : 2
l : 2
m : 2
o : 5
r : 3
s : 5
t : 2
w : 2
y : 1
'''
def solve(words):
    # write your solution from here
    all_freq = {}
    words = str(words)
    for i in words:
        if (i.isalpha()):
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1
    for i in sorted (all_freq) :
        print (i+':',all_freq[i])
'''
Status
Test Cases Passed
Expected Output
Input:
hello these are some awesome words for edyst 
Output:
a: 2
d: 2
e: 8
f: 1
h: 2
l: 2
m: 2
o: 5
r: 3
s: 5
t: 2
w: 2
y: 1
Your Output
Input:
hello these are some awesome words for edyst 
Output:
a: 2
d: 2
e: 8
f: 1
h: 2
l: 2
m: 2
o: 5
r: 3
s: 5
t: 2
w: 2
y: 1
'''