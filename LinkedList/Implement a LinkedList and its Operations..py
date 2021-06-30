'''
Implement a LinkedList and its Operations.
Create a LinkedList with methods given below.
Methods:

insert To insert the value at last in the linked list.
remove To remove the element from LinkedList.
Search To search the element in LinkedList whether the value is present or not (it is boolean method)
insertIndex: To insert the element at particular index.
displayTo display the entire List.
Note:Name of your list must be LinkedList.

Example:

Insert: 1
Insert: 1
Insert: 1
Search for 1. Found: true
Display:
1 1 1 
'''
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

### write LinkedList class below this line ##


class LinkedList:
    def __init__(self):
        self.head=None
        
    def  insert(self,ele):
        new_node=Node(ele)
        if(self.head==None):
            self.head=new_node
            return
        else:
            curr=self.head
            while(curr.next!=None):
                curr=curr.next
            curr.next=new_node
            return
        
    def remove(self,val):
        if(val==self.head.data):
            del_node=self.head
            self.head=self.head.next
            del(del_node)
        else:
            curr=self.head
            while(curr.data!=val):
                prev=curr
                curr=curr.next
            del_node=curr
            prev.next=curr.next
            del(del_node)
            
    def insertIndex(self,ind,element):
        new_node=Node(element)
        if(self.head==None):
            self.head=new_node
        elif(ind==0):
            new_node.next=self.head
            self.head=new_node
        else:
            curr=self.head
            pos=0
            while(pos!=ind):
                prev=curr
                curr=curr.next
                pos=pos+1
            new_node.next=curr
            prev.next=new_node
            
    def Search(self,val):
        if(self.head==None):
            return("false")
        else:
            curr=self.head
            while(curr!=None):
                if(curr.data==val):
                    return("true")
                curr=curr.next
            return("false")
        
    def display(self):
        curr=self.head
        while(curr!=None):
            print(curr.data,end=" ")
            curr=curr.next


'''
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n= n.next
        n.next = new_node

    def remove(self, x):
        if self.head is None:
            #print("",end='')
            return
    # Deleting first node 
        if self.head.data == x:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            return
            #print("",end="")
        else:
            n.next = n.next.next   
            
    def Search(self, x):
        if self.head is None:
            print("",end="")
            return
        n = self.head
        while n is not None:
            if n.data == x:
                return 'true'
            n = n.next
        return 'false'
    
    def insertIndex(self, index, item):
        if index == 1:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node
        i = 1
        n = self.head
        while i < index-1 and n is not None:
            n = n.next
            i = i+1
        if n is None:
            print("",end="")
        else: 
            new_node = Node(item)
            new_node.next = n.next
            n.next = new_node
    def remove(self, item):     
        current = self.head 
        previous = None
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if found and previous is not None:
            previous.set_next(current.get_next())
        elif found and previous is None:
            self.head = None
        else:
            print("",end="")
            
            
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
'''







       







### write LinkedList class above this line ##

if __name__ == "__main__": 
    test_cases=int(input()) # number of test cases
    myList=LinkedList()

    while(test_cases>0):
        instruction=int(input()) # current instruction
        ####
        # 1 means insertion
        # 2 means remove value
        # 3 means search value
        # 4 means insert at particular index
        # 5 means display entire list
        ####

        if(instruction==1): 
            val=int(input())
            print(f'Insert: {val}')
            myList.insert(val)
        elif (instruction==2):
            val=int(input())
            print(f'Delete: {val}')
            myList.remove(val)
        elif (instruction==3):
            val=int(input())
            print(f'Search for {val}. Found: {myList.Search(val)}')
        elif(instruction==4):
            index=int(input())
            val=int(input())
            print(f'Insert {val} at index {index}')
            myList.insertIndex(index,val)
        elif(instruction==5):
            print('Display:')
            myList.display()
            print()
        
        test_cases=test_cases-1

'''
Status
Test Cases Passed
Input
5
1
1
1
1
1
1
3
1
5
Expected Output
Insert: 1
Insert: 1
Insert: 1
Search for 1. Found: true
Display:
1 1 1 
Your Output
Insert: 1
Insert: 1
Insert: 1
Search for 1. Found: true
Display:
1 1 1 
'''