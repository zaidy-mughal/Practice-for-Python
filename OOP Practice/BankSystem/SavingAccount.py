from BankAccount import BankAccount

class SavingAccount(BankAccount):

    """This class is designed to perform Saving Account Functions which is inherited from Bank Account Class"""

    withdrawfee = 50

    def __init__(self, accountId, userName, totalBalance,accountType,interestRate):
        super().__init__(accountId, userName, totalBalance,accountType)
        self.interestRate = interestRate
    
    def deposit(self, depositAmount):
        depositAmount += (self.interestRate/100)*depositAmount
        super().deposit(depositAmount)
    
    def withdraw(self, withdrawAmount):
        withdrawAmount += self.withdrawfee
        super().withdraw(withdrawAmount)
    
    def checkBalance(self):
        return super().checkBalance()

    def __str__(self) -> str:
        return super().__str__()