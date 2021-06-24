'''
Swap dictionary values
Complete the given method called solve which takes as parameter a dictionary A.

A has some keys, but the values of the keys 'x' and 'y' have been mistakenly swapped. You have to put them back in their original positions, And return the dictionary.

Example Input:
{'a': 1, 'b': 200, 'x': 2, 'y': 7}
 
Output:
{'a': 1, 'b': 200, 'x': 7, 'y': 2}

'''
def solve(d):
    # write your logic from here
    
    
    
    #d['x'], d['y'] = d['y'], d['x']
    '''
    new_dict = {}
    for x, y in d.items():
        new_dict[x] = y
    '''
    d['x'],d['y']= d['y'],d['x']
    return(d)

'''
Status
Test Cases Passed
Expected Output
Input:
a:1
b:200
x:2
y:7

Output:
a:1
b:200
x:7
y:2
Your Output
Input:
a:1
b:200
x:2
y:7

Output:
a:1
b:200
x:7
y:2
'''