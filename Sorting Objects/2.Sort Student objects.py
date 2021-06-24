'''
Sort Student objects
Given the following Student class:

class Student:
	def __init__(self, name, roll_number):
    	self.name = name
        self.roll_number = roll_number
Complete the given method solve which takes as parameter a list A of Student objects.

You must print all the Student objects in ascending order of their names.

Example Input:
Jim 19025 | Dwight 3297 | Pam 12301 | Erin 12093 | 
Output:
Dwight 3297 | Erin 12093 | Jim 19025 | Pam 12301 | 

'''
def solve(A):
    # your code below this line
    def getName(student):
        return student.name
    A.sort(key=getName)
    for student in A:
        print(student.name + ' ' + str(student.roll_number) +' | ',end = '')
'''
Status
Test Cases Passed
Expected Output
Input:
Jim 19025 | Dwight 3297 | Pam 12301 | Erin 12093 | 
Output:
Dwight 3297 | Erin 12093 | Jim 19025 | Pam 12301 | 
Your Output
Input:
Jim 19025 | Dwight 3297 | Pam 12301 | Erin 12093 | 
Output:
Dwight 3297 | Erin 12093 | Jim 19025 | Pam 12301 | 
'''