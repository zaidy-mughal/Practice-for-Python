class BankAccount:
    def __init__(self,accountId,userName,totalBalance,accountType):
        self.accountId = accountId
        self.userName = userName
        self.totalBalance = totalBalance
        self.accountType = accountType


    def deposit(self,depositAmount):
        totalBalance += depositAmount
        return totalBalance

    def withdraw(self,withdrawAmount):
        if totalBalance >= withdrawAmount:
            totalBalance -= withdrawAmount
            return totalBalance
        else:
            print("You did'nt have enough balance")
            return -1

    def checkBalance(self):
            return self.totalBalance
    