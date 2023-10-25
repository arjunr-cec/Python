row=int(input("Enter the number of rows:"))
step=int(input("Enter the step number:"))
for i in range(1,row+1,step):
    for j in range(1,i+1,step):
      print(i*j,end=" ")
    print("\n")
