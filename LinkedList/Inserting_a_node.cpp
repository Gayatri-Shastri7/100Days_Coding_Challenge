'''
Inserting a node
Given the pointer to the head node of a linked list, an integer to add to the list and the position at which the integer must be inserted.
Create a new node with the given integer, insert this node at the desired position and return the head node.
A position of 0 indicates head, a position of 1 indicates one node away from the head and so on.

Note: The head pointer given may be null meaning that the initial list is empty.
Example :
Input :
A. 1->2->3
position = 2
data = 4

Output :
A. 1->2->4->3
'''

struct Solution {
  LLNode * insertNodeAtPosition(LLNode *head, int data, int position) {
      /* write your solution here */
      LLNode * newnode = (LLNode *)malloc(sizeof(LLNode));
    newnode->val=data;
    LLNode *temp=head,*prev;
    if(position==0){
        newnode->next=head;
        head=newnode;
        return head;
    }
    else{
        while(position--){
            prev=temp;
            temp=temp->next;
        }
        prev->next=newnode;
        newnode->next=temp;
        return head;
    
    }
        
}
};
// Status
// Test Cases Passed
// Expected Output
// INPUT(s):
// 1 
// 4
// 1

// OUTPUT(s):
// 1 4 

// INPUT(s):
// 4 
// 8
// 0

// OUTPUT(s):
// 8 4 

// INPUT(s):
// 1 4 6 7 
// 4
// 1

// OUTPUT(s):
// 1 4 4 6 7 

// Your Output
// INPUT(s):
// 1 
// 4
// 1

// OUTPUT(s):
// 1 4 

// INPUT(s):
// 4 
// 8
// 0

// OUTPUT(s):
// 8 4 

// INPUT(s):
// 1 4 6 7 
// 4
// 1

// OUTPUT(s):
// 1 4 4 6 7 