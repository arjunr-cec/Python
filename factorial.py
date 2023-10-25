def fact(num):
    f=1
    if num==0:
        print("factorial is:",f)
    elif num<0:
        print("can't find the factorial")
    else:
        for i in range(1,num+1):
            f=f*i
        print("factoial of",num,"is",f)
num=int(input("enter the no to find factorial"))
fact(num)
