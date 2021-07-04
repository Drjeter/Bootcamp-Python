# In the last assignment, your code might have looked something like this:

# guido.make_deposit(100)
# guido.make_deposit(200)
# guido.make_deposit(300)
# guido.make_withdrawal(50)
# guido.display_user_balance()
# 
# This takes up a lot of space and we're repeating our call to guido many times. There is a way to call on guido just once and keep attaching 
# new method calls to the end of the previous one, like so:

# guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()
# 
# This is called chaining. In order for this to work, each method must return self. By returning self, if we recall how functions work, each method 
# call will now be equal to the instance that called it.

# For example if guido.make_deposit(100) returns its own instance (guido), then we can call one of that instance's methods after that call, 
# like guido.make_deposit(100).make_withdrawal(50).

# class User:
#     def make_deposit(self, amount):
#         # your code goes here...
#         return self
# copy
# The practice of having OOP return its own instance is pretty common and is done in other programming languages, 
# though the variable name in some languages is not self, but instead this.

# Update your previous assignment so that each instance's methods are chained

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self
    # adding the withdrawal method
    def make_withdrawal(self, amount):  # takes an argument that is the amount of the withdrawal
        self.account_balance -= amount  # the specific user's account increases by the amount of the value received
        return self
    # adding the display_user_balance method
    def display_user_balance(self): 
        print(self.name, "has $" + str(self.account_balance))
        return self
    # adding the transfer_money method
    def transer_money(self, other_user, amount): # takes two argument: amount of the transfer and user to transfer to
        self.account_balance -= amount # the transferring user's account decreases by the transfer amount
        other_user.account_balance += amount # the other user's account increases by the transfer amount
        return self

lydia = User("Lydia", "lydia@fofo.com")
fayez = User("Fayez", "Fayez@bcs.com")
karim = User("Karim", "Karim@Apeak.com")

lydia.make_deposit(100).make_deposit(500).make_deposit(50).make_withdrawal(250).display_user_balance()
fayez.make_deposit(1000).make_deposit(250).make_withdrawal(600).make_withdrawal(600).display_user_balance()
karim.make_deposit(200).make_withdrawal(20).make_withdrawal(75).make_withdrawal(13).display_user_balance()
lydia.transer_money(karim, 300).display_user_balance()
karim.display_user_balance()