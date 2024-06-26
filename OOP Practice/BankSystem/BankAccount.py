class BankAccount:

    """This is the base class for Checking Account and Saving Account"""

    def __init__(self,accountId,userName,totalBalance,accountType):
        self.accountId = accountId
        self.userName = userName
        self.totalBalance = totalBalance
        self.accountType = accountType


    def deposit(self,depositAmount):
        self.totalBalance += depositAmount
        print(depositAmount," with Interest Successfully Deposited! ")

    def withdraw(self,withdrawAmount):
        if self.totalBalance >= withdrawAmount:
            self.totalBalance -= withdrawAmount
            print(withdrawAmount, ' is Successfully withdrawed from your account!')
        else:
            print("You did'nt have enough balance")

    def checkBalance(self):
            return self.totalBalance
    
    def __str__(self) -> str:
        return (f"\n---Account Details---\n"
                f"User Name: {self.userName}\n"
                f"Account ID: {self.accountId}\n"
                f"Account Type: {self.accountType}\n"
                f"Total Balance: {self.totalBalance}")