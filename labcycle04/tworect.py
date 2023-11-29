class Rectangle:
    area=0
    perimeter=0
    def __init__(self,length,width):
        self._length=length
        self._width=width
        self._area = 0
    def calc_area(self):
        self._area = self._length * self._width
        print("area is:", self._area)
    def is_larger(self, other):
        return self._area < other._area
        
length1=int(input("enter the length of the rectangle1:"))
width1=int(input("enter the width of the rectangle1:"))
length2=int(input("enter the length of the rectangle2:"))
width2=int(input("enter the width of the rectangle2:"))

obj1 = Rectangle(length1, width1)
obj2 = Rectangle(length2, width2)
obj1.calc_area()
obj2.calc_area()
if obj1.is_larger(obj2):
    print("Rectangle 2 is larger")
else:
    print("Rectangle 1 is larger")

