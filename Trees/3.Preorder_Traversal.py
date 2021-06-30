'''
Preorder Traversal (A)
Given a binary tree, return the preorder traversal of its nodes’ values.

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
[1, 2, 3]
Your Answer
Language

'''
class Solution:
    def preorderTraversal(self, root):
        # write your method here
        if not root:
            return []
        res = []
        res.append(root.val)
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
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
2 2 1 

INPUT(s):
4 3 -1 2 4 -1 -1 -1 -1 

OUTPUT(s):
4 3 2 4 

Your Output
INPUT(s):
2 -1 -1 

OUTPUT(s):
2

INPUT(s):
2 2 -1 1 -1 -1 -1 

OUTPUT(s):
2 2 1

INPUT(s):
4 3 -1 2 4 -1 -1 -1 -1 

OUTPUT(s):
4 3 2 4

'''