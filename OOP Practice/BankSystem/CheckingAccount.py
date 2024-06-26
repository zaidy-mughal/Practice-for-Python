from BankAccount import BankAccount

class CheckingAccount(BankAccount):

    """This class is created to manage checking account operations and it is inherited from"""

    def __init__(self,accountId,userName,totalBalance,accountType,interestRate):
        super().__init__(accountId,userName,totalBalance,accountType)
        self.interestRate = interestRate

    def deposit(self,depositAmount):
        depositAmount += (self.interestRate/100)*depositAmount
        super().deposit(depositAmount)
    
    
    def withdraw(self,withdrawAmount):
        super().withdraw(withdrawAmount)
    
    def checkBalance(self):
        return super().checkBalance()