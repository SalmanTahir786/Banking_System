# Banking System Requirements:
# implements OOP concepts
# Creates user account
# User can deposit, withdraw cash as well as transfer to other Users
# User can view his/her account details
# Maintain Transaction history
# 1. Create Account
# 2. Display Accounts
# 3. Deposit Amount
# 4. Withdraw Amount
# 5. Transfer Amount
# 6. Transaction History of specific account
# 7. Transaction History
# 8. Exit

class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_detail(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("age ", self.age)
        print("gender ", self.gender)



