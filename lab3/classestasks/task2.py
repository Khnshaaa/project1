#Define a class named Shape and its subclass 
# Square. The Square class has an init function which
# takes a length as argument. Both classes have 
# a area function which can print the area of 
# the shape where Shape's area is 0 by default.

class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0 
class square (Shape):
    def __init__(self,length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length*self.length

if __name__ == "__main__":
    s = square(5)
    print(s.area())
    s1 = Shape()
    print(s1.area())