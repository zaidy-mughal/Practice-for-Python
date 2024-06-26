from BankAccount import BankAccount
from SavingAccount import SavingAccount
from CheckingAccount import CheckingAccount
import random

print("\n====== Bank Management System ======\n")

bank = None

while True:
    print("\n1. Create Account (If new user)")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Check Current Account Balance")
    print("5. View your Account Details")
    print("5. Press Other than 1-5 to Close.")

    choice = int(input("\nEnter your choice: "))
    
    if choice == 1:
        userName = input('Enter your User Name: ')
        accountId = random.randint(10,99)
        totalBalance = float(0)
        accountType = input('Which type of account do you want to open\nType saving or checking: ')
        if accountType == "saving":
            saving_acc = SavingAccount(accountId,userName,totalBalance,    accountType,float(5))
            bank: BankAccount = saving_acc
        elif accountType == 'checking':
            checking_acc = CheckingAccount(accountId,userName,totalBalance,  accountType,float(2.5))
            bank: BankAccount = checking_acc
        else:
            print('Invalid Account Type!')
            


    elif choice == 2:
        if bank is not None:
            depositAmount = float(input('Enter the amount to deposit: '))
            bank.deposit(depositAmount)
        else:
            print('Create Account First then deposit! ')
        
    elif choice == 3:
        if bank is not None:
            withdrawAmount = float(input('Enter the amount to Withdraw: '))
            bank.withdraw(withdrawAmount)
        else:
            print('Create Account First then Withdraw! ')
        
        
    elif choice == 4:
        if bank is not None:
            balance = bank.checkBalance()
            print('Your total Balance is: ',balance)
        else:
            print('Create Account First then CheckBalance! ')
        
    elif choice == 5:
        if bank is not None:
            print(bank)
        else:
            print('Create Account First then Check Details! ')
        
    else:
        print('Thanks for using!')
        break

