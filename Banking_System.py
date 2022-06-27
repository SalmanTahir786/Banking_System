class BankAccount:
    no_of_customer = 0
    account_num = 5000

    def __init__(self, name, mobile_no, initial_depo, pin):

        self.name = name
        self.cust_acc_num = BankAccount.account_num
        self.mobile_no = mobile_no
        self.acc_balance = initial_depo
        self.pin = pin

        BankAccount.no_of_customer = BankAccount.no_of_customer + 1
        BankAccount.account_num = BankAccount.account_num + 1

    def basic_details(self):
        print(f'User: {self.name}\t Account No: {self.cust_acc_num}\t Balance: ${self.acc_balance}')

    def deposit(self):
        amount = int(input('Enter the deposit amount: '))
        if amount > 0:
            self.acc_balance = self.acc_balance + amount
            print(f'Transaction completed. Current Balance: ${self.acc_balance}')
        else:
            print('Invalid amount transaction')

    def withdrawl(self):
        amount = int(input('Enter the withdrawl amount: '))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance = self.acc_balance - amount
            print(f'Transaction completed. Current Balance: ${self.acc_balance}')
        else:
            print('Invalid amount transaction')

    def payment(self, other):
        amount = int(input('Enter the payment amount: '))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance = self.acc_balance - amount
            other.acc_balance = other.acc_balance + amount
            print(f'Transaction completed. Current Balance: ${self.acc_balance}')
        else:
            print('Invalid amount transaction')
