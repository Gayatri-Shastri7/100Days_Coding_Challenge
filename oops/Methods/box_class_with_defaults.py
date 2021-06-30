'''
The Box Class, with defaults
Write the Box class. Every Box object must have height, width and breadth.

Write the __init__ method that initializes these values. However, if no value is passed, take the default values to be:
height, 20
width, 30
breadth, 3
Also write a method volume that returns the volume of the box
'''
class Box:
    def __init__(self,height=20,width=30,breadth=3):
        self.height = height
        self.width= width
        self.breadth = breadth
    def volume(self):
        return(self.width*self.height*self.breadth)




## your code above this line ##

height = int(input())
width = int(input())
breadth = int(input())

box1 = Box(height,width,breadth)

print(f"box1 of height: {box1.height}, width: {box1.width} and breadth: {box1.breadth}")
print(f"box1 has volume: {box1.volume()}")

box2 = Box()

print(f"box2 of height: {box2.height}, width: {box2.width} and breadth: {box2.breadth}")
print(f"box2 has volume: {box2.volume()}") 

'''
Status
Test Cases Passed
Input
4
5
6
Expected Output
box1 of height: 4, width: 5 and breadth: 6
box1 has volume: 120
box2 of height: 20, width: 30 and breadth: 3
box2 has volume: 1800
Your Output
box1 of height: 4, width: 5 and breadth: 6
box1 has volume: 120
box2 of height: 20, width: 30 and breadth: 3
box2 has volume: 1800
'''