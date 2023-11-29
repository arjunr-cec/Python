class bank:
    def __init__(self,accno,name,accty,bal):
        self.accno=accno
        self.name=name
        self.accty=accty
        self.bal=0
    def showamt(self):
        print("account holderr name:",self.name)
        print("account number:",self.accno)
        print("account type:",self.accty)
        print("your balance amount:",self.bal)
    def depo(self,d1):
        self.bal=self.bal+d1
        return self.bal
    def withd(self,w1):
        self.bal=self.bal-w1
        return self.bal
    n=input("enter your name:")
    a=int(input("enter your account number:"))
    t=input("enter your account type:")
    o=bank(a,n,t,bal0)
    o.showamt()
    while(True):
        print("\n menu")
        print("\n1.deposit")
        print("\n2.withdraw")
        c=int(input("enter yoyr choice:"))
        if(c==1):
            d=int(input("enter your choice:"))
            print("your total balance is:",o.depo(d))
        elif(c==2):
            w=int(input("enter the amount to be withdrawed:"))
            if(w>d):
                print("INSUFFICIENT FUND")
            else:
                print("your total balance amount is",o.withd(w))
        else:
                print("enter a valid choice:")
        
