'''
Sum of Marks
Complete the given method called solve which takes as parameter a list of dictionaries called marks

Each element represents the marks of the students in different subjects.

You have to find out:

Name of student with maximum marks in English
Name of student with highest sum of marks
Each element (dictionary) is guaranteed to have a name key

Example Input:
{'name': 'Jim', 'English': 92, 'Math': 80, 'Physics': 70}
{'name': 'Pam', 'French': 72, 'English': 80, 'Biology': 65}
{'name': 'Dwight', 'Farming': 95, 'English': 85, 'Chemistry': 97}
 
Output:
Max English: Jim
Max Marks: Dwight
'''
def solve(marks):
    # write your code from here
    MaxEnglish = 0
    MaxMarks = 0
    m = 0
    res1 = ''
    res2 = ''
    for i in marks:
        if(i['English'] > MaxEnglish):
            MaxEnglish = i['English']
            res1 = i['name']
    print("Max English:",res1)
    for i in marks:
        for j in i:
            if(j != 'name'):
                m = m + i[j]
            else:
                if(m > MaxMarks):
                    MaxMarks = m
                    res2 = i['name']
                m = 0
            if(m > MaxMarks):
                MaxMarks = m
                res2 = i['name']
    print("Max Marks:",res2)
'''
Status
Test Cases Passed
Expected Output
Input:
{'name': 'Jim', 'English': 92, 'Math': 80, 'Physics': 70}
{'name': 'Pam', 'French': 72, 'English': 80, 'Biology': 65}
{'name': 'Dwight', 'Farming': 95, 'English': 85, 'Chemistry': 97}
Output:
Max English: Jim
Max Marks: Dwight
Your Output
Input:
{'name': 'Jim', 'English': 92, 'Math': 80, 'Physics': 70}
{'name': 'Pam', 'French': 72, 'English': 80, 'Biology': 65}
{'name': 'Dwight', 'Farming': 95, 'English': 85, 'Chemistry': 97}
Output:
Max English: Jim
Max Marks: Dwight
'''