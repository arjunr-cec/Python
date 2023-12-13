class Publisher:
 def __init__(self, pbname):
  self.pbname = pbname
 def display(self):
  return (self.pbname)
class Book(Publisher):
 def __init__(self, title, author, pbname):
  self.title = title
  self.author = author
  Publisher.__init__(self, pbname)
 def display(self):
  return (self.pbname, self.title, self.author)
class Python(Book):
 def __init__(self, price, pages, title, author, pbname):
  self.price = price
  self.pages = pages
  Book.__init__(self, title, author, pbname)
 def display(self):
  print("Publisher :", self.pbname)
  print("Title :", self.title)
  print("Author :", self.author)
  print("Price :", self.price)
  print("Pages :", self.pages)
pbname=input("Enter the publisher name - ")
title=input("Enter the title name - ")
author=input("Enter the author name - ")
price=int(input("Enter the price - "))
pages=int(input("Enter the number of pages - "))
print("Book Details:")
obj=Python(price, pages, title, author, pbname)
#obj = Python(179, 456, "Wings of Fire ", "A P J Abdul Kalam", "DC Books")
obj.display()
