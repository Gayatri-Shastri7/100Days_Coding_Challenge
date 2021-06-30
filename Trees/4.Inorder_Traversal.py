'''
Inorder Traversal (A)
Given a binary tree, return the inorder traversal of its nodes’ values.

Example :
Input :
Given binary tree

1
 \
  2
 /
3
The input is presented as:
1 -1 2 3 -1 -1 -1 (here -1 represents null)

Please note that the above is only a representation of the input. In the answer, please use the head node to traverse through the tree

Output :
[1, 3, 2]
'''
"""
reference data types:

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""

class Solution:
    def inorderTraversal(self, root):
        # write your method here
        if not root:
            return []
        
        res = []
        res += self.inorderTraversal(root.left)
        res.append(root.val)
        res += self.inorderTraversal(root.right)
        return res
'''
Status
Test Cases Passed
Expected Output
INPUT(s):
2 -1 -1 

OUTPUT(s):
2 

INPUT(s):
2 2 -1 1 -1 -1 -1 

OUTPUT(s):
1 2 2 

INPUT(s):
4 3 -1 2 4 -1 -1 -1 -1 

OUTPUT(s):
2 3 4 4 

Your Output
INPUT(s):
2 -1 -1 

OUTPUT(s):
2

INPUT(s):
2 2 -1 1 -1 -1 -1 

OUTPUT(s):
1 2 2

INPUT(s):
4 3 -1 2 4 -1 -1 -1 -1 

OUTPUT(s):
2 3 4 4

'''