num=int(input("Enter the number to find factor"))
print("factors of",num,"are\n")
for i in range(1,num+1):
    if num%i==0:
       print(i)
        
