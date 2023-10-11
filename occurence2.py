len = int(input("how many elements you want to enter:"))
list = []
for i in range (0,len):
    value=int(input("enter the value"))
    if value>100:
       list.append('over')
    else:
        list.append(value)
    print(list)
