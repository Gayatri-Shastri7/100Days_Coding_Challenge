'''
Implement a Queue and its operations
Write a program to create a Queue and it's operations which is given below.  Name you class as Queue. In Queue class use Integer array to implement Queue. Check the code for more details.

Operations:

enque accepts an integer and adds to the Queue
deque remove the element from Queue and prints the value which is removed.
peek it returns the latest element from the queue
isEmpty returns true if Queue is empty, and false otherwise
isFull returns true if Queue is Full, and false otherwise
'''
class Queue:
    
    def __init__(self,n):

        self.data=[]

        self.number=n

        self.front=self.rear=0

    def enque(self,element):

        if(self.rear!=self.number):

            self.data.append(element)

            self.rear += 1

    def deque(self):

        if(self.front!=self.rear):

            x=self.data.pop(0)

            print("deque:"+str(x))

            self.rear -= 1

        else:

            print("deque:"+"None")

    def peek(self):

        return self.data[0]

    def isEmpty(self):

        if(self.rear==0):

            return "true"

        else:

            return "false"

    def isFull(self):

        if(self.rear==self.number):

            return "true"

        else:

            return "false"
'''
Status
Test Cases Passed
Input
6
5
1 1
1 2
4
5
2
3
Expected Output
enque:1
enque:2
isEmpty:false
isFull:false
deque:1
peek:2
Your Output
enque:1
enque:2
isEmpty:false
isFull:false
deque:1
peek:2
'''