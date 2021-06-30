# The Box Class
# The Box Class
# Write the Box class. Every Box object must have height, width and breadth.

# Write the __init__ method that initializes these values
# Also write a method volume that returns the volume of the box
# Write only the Box class. The rest of the code has been written. Check the remaining code to understand how the input is being taken.

class Box:
    def __init__(self,height,width,breadth):
        self.height = height
        self.width = width
        self.breadth = breadth
    def volume(self):
        return(height*width*breadth)


## your code above this line ##

height = int(input())
width = int(input())
breadth = int(input())

box1 = Box(height,width,breadth)

print(f"box1 of height: {box1.height}, width: {box1.width} and breadth: {box1.breadth}")
print(f"box1 has volume: {box1.volume()}")

'''
Test Cases Passed
Input
2
3
5
Expected Output
box1 of height: 2, width: 3 and breadth: 5
box1 has volume: 30
Your Output
box1 of height: 2, width: 3 and breadth: 5
box1 has volume: 30
'''