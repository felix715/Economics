class Bank:
    def __init__(self):
        self.Balance = 0
        print("The New account is created.")

    def deposit(self):
        amount=float(input("Enter the amount to be deposited: "))
        self.Balance=self.Balance+amount
        print("The deposit is successful and the balance in the account is ksh",self.Balance)

    def withdraw(self):
        amount_with=float(input("Enter the amount to be withdrawn: "))
        if (self.Balance>=amount_with):
            self.Balance=self.Balance-amount_with
            print("Withdrawn amount is successful and balance is ksh",self.Balance)
        else:
            print("Insufficient balance: ")

    def enquiry(self):
        print("Balance in the account is ksh",self.Balance)


acc=Bank()
acc.deposit()
acc.withdraw()
