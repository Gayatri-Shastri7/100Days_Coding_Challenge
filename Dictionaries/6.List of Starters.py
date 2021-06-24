'''
List of Starters
Jim and Pam are visiting a restaurant. The restaurant has many items. They want to know the list of elements that start with each alphabet. We may ignore those alphabets that don't have any items.

Complete the given method called solve which takes as parameter a list of strings called items.

You have to print the list of items for each alphabet. Print in sorted order of alphabets.

Example Input:
noodles, rice, banan, sweets, ramen, souffle, apricot, apple, bread
 
Output:
a : apple apricot
b : banana bread
n : noodles
r : ramen rice
s : souffle sweets
'''

def solve(items):

    # writ

    c = 0

    d = {}

    for i in items:

        k = i[0]

        if(i.startswith(k)):

            d.setdefault(k, []).append(i)

    for i in sorted (d) :

        str = ' '.join(sorted(d[i]))

        print (i,':',str)
'''
Status
Test Cases Passed
Expected Output
Input:
noodles rice banana sweets ramen souffle apricot apple bread 
Output:
a : apple apricot 
b : banana bread 
n : noodles 
r : ramen rice 
s : souffle sweets 
Your Output
Input:
noodles rice banana sweets ramen souffle apricot apple bread 
Output:
a : apple apricot
b : banana bread
n : noodles
r : ramen rice
s : souffle sweets
'''