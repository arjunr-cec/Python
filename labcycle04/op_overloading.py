class rectangle:
 def __init__(self):
  self._length = int(input("Enter the Length:"))
  self._breadth = int(input("Enter the Breadth:"))
  self.area = self._length * self._breadth
 def greaterThan(self, rectangle):
  if self.area < rectangle.area:
   print("Area of rectangle 1 is Greater")
  else:
   print("Area of rectangle 2 is Greater")
print("Rectangle 1:")
r1 = rectangle()
print("Rectangle 2:")
r2 = rectangle()
print("Comparing Rectangles:")
r2.greaterThan(r1)
