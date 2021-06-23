'''
Deleting from a BST
Given a root node reference of a BST and a key, delete the node with the given key in the BST.
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).
Example :
Input :
    
         5
        / \
       3   6
      / \   \
     2   4   7
key = 3

Output :
    one valid answer is  
        5
       / \
      4   6
     /     \
    2       7
 
    another valid answer
       5
      / \
      2   6
       \   \
        4   7
    you can do any of them.

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
    def deleteNode(self, root, key):
        # write your method here
        if not root:
            return None
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left and root.right:
                delNode = self.find_min(root.right)
                root.val = delNode.val
                root.right = self.deleteNode(root.right, delNode.val)
            elif root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                root = None
                
        return root
        
    
    def find_min(self, node):
        if not node.left:
            return node
        return self.find_min(node.left)
'''
Status
Test Cases Passed
Expected Output
INPUT(s):
7 2 19 -1 -1 8 23 -1 10 -1 -1 -1 -1 
19

OUTPUT(s):
correct

INPUT(s):
2 -1 5 3 6 -1 4 -1 7 -1 -1 -1 14 -1 -1 
4

OUTPUT(s):
correct

INPUT(s):
4 2 6 1 3 -1 -1 -1 -1 -1 -1 
32

OUTPUT(s):
correct

Your Output
INPUT(s):
7 2 19 -1 -1 8 23 -1 10 -1 -1 -1 -1 
19

OUTPUT(s):
correct

INPUT(s):
2 -1 5 3 6 -1 4 -1 7 -1 -1 -1 14 -1 -1 
4

OUTPUT(s):
correct

INPUT(s):
4 2 6 1 3 -1 -1 -1 -1 -1 -1 
32

OUTPUT(s):
correct

'''