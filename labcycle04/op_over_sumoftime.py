class Time:
 def __init__(self, hour, minute, second):
  self.hour = hour
  self.minute = minute
  self.second = second
 def __add__(self, other):
  return self.hour + other.hour, self.minute + other.minute, self.second + other.second
o1 = Time(2, 40, 10)
o2 = Time(4, 20, 50)
print("Sum of Time: ",o1 + o2)
