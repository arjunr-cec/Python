n1=int(input("no of elements in the first list:"))
list1=[]
for i in range (n1):
    value=int(input("enter the elements:"))
    list1.append(value)
n2=int(input("no of elements in the second list:"))
list2=[]
for i in range(n2):
    value=int(input("input no:"))
    list2.append(value)
if(n1==n2):
    print("same length")
else:
    print("not same length")
if(sum(list1)==sum(list2)):
    print("same sum")
else:
    print("sum are different")
list3=[each for each in list1 if each in list2]
print("same numbers are:",list3)

