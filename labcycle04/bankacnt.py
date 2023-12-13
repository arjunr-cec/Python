class Bank:
    def __init__(self, accno, name, accty):
        self.accno = accno
        self.name = name
        self.accty = accty
        self.bal = 0

    def showamt(self):
        print("Account holder name:", self.name)
        print("Account number:", self.accno)
        print("Account type:", self.accty)
        print("Your balance amount:", self.bal)

    def depo(self, d1):
        self.bal = self.bal + d1
        return self.bal

    def withd(self, w1):
        if w1 > self.bal:
            print("INSUFFICIENT FUNDS")
        else:
            self.bal = self.bal - w1
            return self.bal

n = input("Enter your name:")
a = int(input("Enter your account number:"))
t = input("Enter your account type:")
account = Bank(a, n, t)

account.showamt()

while True:
    print("\n Menu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        deposit_amount = int(input("Enter the deposit amount:"))
        print("Your total balance is:", account.depo(deposit_amount))
    elif choice == 2:
        withdraw_amount = int(input("Enter the amount to be withdrawn:"))
        print("Your total balance amount is", account.withd(withdraw_amount))
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Enter a valid choice:")
