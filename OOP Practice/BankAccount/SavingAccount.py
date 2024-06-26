from BankAccount import BankAccount

class SavingAccount(BankAccount):

    """This class is designed to perform Saving Account Functions which is inherited from Bank Account Class"""

    withdrawfee = 50

    def __init__(self, accountId, userName, totalBalance,accountType):
        super().__init__(accountId, userName, totalBalance)
    
    def deposit(self, depositAmount):
        payment += (self.interestRate/100)*depositAmount
        return super().deposit(payment)
    
    def withdraw(self, withdrawAmount):
        withdrawAmount += self.withdrawfee
        return super().withdraw(withdrawAmount)
    
    def checkBalance(self):
        return super().checkBalance()
