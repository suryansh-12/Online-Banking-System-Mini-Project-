import sys
class Customer:
    '''Customer class for Banking'''
    bankname = 'HDFC Bank'
    def __init__(self,name,balance = 0):
        self.name = name
        self.balance = balance
        print('Welcome to HDFC',self.name)
    def deposit(self,amount):
        self.balance = self.balance + amount
        print('After Deposit your Account Balance is :',self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("Sorry Insufficient Balance")
            sys.exit()
        self.balance = self.balance - amount
        print('Withdraw Successfully..\n Your current account balance is:',self.balance)
print('Welcome to',Customer.bankname)
name = input('Enter your Name :')
c = Customer(name)
while True:
    print('D-Deposit\nW-Withdraw\nE-Exit')
    option = input('Choose an Option:')
    if option.upper()=='D':
        amount = float(input('Enter the Amount to Deposit'))
        c.deposit(amount)
    elif option.upper()=='W':
        amount = float(input('Enter amount to withdraw'))
        c.withdraw(amount)
    elif option.upper()=='E':
        print('Thanks for using HDFC Bank \n HAVE A NICE DAY')
    else:
        print('Choose Valid Option')
