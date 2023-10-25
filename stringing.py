def addstr(str):
    l=len(str)
    if l>0:
        if str[-3:]=="ing":
            str+="ly"
        else:
            str+="ing"
    print(str)
str=input("Enter the String:")
addstr(str)
    
