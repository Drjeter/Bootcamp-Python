# Update your existing User class to have an association with the BankAccount class. You should not have to change anything in the BankAccount class. 
# The method signatures of the User class (the first line of the method with the def keyword) should also remain the same.

# For example, our User class currently has a method like this:

# class User:
#     # other methods
#     def make_deposit(self, amount):
#     	self.account_balance += amount	# hmmm...the User class doesn't have an account_balance attribute anymore
# 
# But for this assignment, our User class will no longer have a self.account_balance attribute. Instead, we will replace this attribute's value in our __init__ 
# method with an instance of a BankAccount, and use the name of self.account. That means our make_deposit (and other methods referencing self.account_balance) 
# need to be updated! That's the goal of this assignment.

# Remember in our User methods, we are going to now be accessing the BankAccount class through our self.account attribute, like so:

# class User:
#     def example_method(self):
#         self.account.deposit(100)		# we can call the BankAccount instance's methods
#     	print(self.account.balance)		# or access its attributes
#
# Make sure that by the end of this assignment that you:

# have both the User and BankAccount classes in the same file for your assignment
# only create BankAccount instances inside of the User's __init__ method
# only call BankAccount methods inside of the methods in the User class
# Update the User class __init__ method

# Update the User class make_deposit method

# Update the User class make_withdrawal method

# Update the User class display_user_balance method

# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

class BankAccount:
    def __init__(self, int_rate = .01, balance = 0): # don't forget to add some default values for these parameters!
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print("Balance: $" + str(self.balance))
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance*self.int_rate
        return self

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}
    # adding the add_accout method
    def add_account(self, name):
        self.accounts[name] = BankAccount()
        return self.accounts[name]
    # adding the deposit method
    def make_deposit(self, account, amount):	# takes an argument that is the amount of the deposit
        self.accounts[account].balance += amount	# the specific user's account increases by the amount of the value received
        return self.accounts[account]
    # adding the withdrawal method
    def make_withdrawal(self, account, amount):  # takes an argument that is the amount of the withdrawal
        self.accounts[account].balance -= amount  # the specific user's account increases by the amount of the value received
        return self.accounts[account]
    # adding the display_user_balance method
    def display_user_account_balance(self, account): 
        print(self.name, "has $" + str(self.accounts[account].balance))
        return self.accounts[account]
    # adding the transfer_money method
    def transer_money(self, account, other_account_user, other_account_name, amount): # takes two argument: amount of the transfer and user to transfer to
        self.accounts[account].balance -= amount # the transferring user's account decreases by the transfer amount
        other_account_user.accounts[other_account_name].balance += amount # the other user's account increases by the transfer amount
        return self.accounts[account]

lydia = User("Lydia", "lydia@fofo.com")
lydia.add_account("checking")
lydia.add_account("savings")
lydia.accounts["savings"].deposit(100).withdraw(200).yield_interest().display_account_info()
lydia.accounts["checking"].deposit(500).deposit(1000).withdraw(250).yield_interest().display_account_info()
lydia.transer_money("checking", lydia, "savings", 262.5)
lydia.accounts["savings"].display_account_info()
lydia.accounts["checking"].display_account_info()
