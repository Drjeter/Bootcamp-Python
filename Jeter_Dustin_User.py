# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
#
#  Create a file with the User class, including the __init__ and make_deposit methods

# Add a make_withdrawal method to the User class

# Add a display_user_balance method to the User class

# Create 3 instances of the User class

# Have the first user make 3 deposits and 1 withdrawal and then display their balance

# Have the second user make 2 deposits and 2 withdrawals and then display their balance

# Have the third user make 1 deposits and 3 withdrawals and then display their balance

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
    # adding the withdrawal method
    def make_withdrawal(self, amount):  # takes an argument that is the amount of the withdrawal
        self.account_balance -= amount  # the specific user's account increases by the amount of the value received
    # adding the display_user_balance method
    def display_user_balance(self): 
        print(self.name, "has $" + str(self.account_balance))
    # adding the transfer_money method
    def transer_money(self, other_user, amount): # takes two argument: amount of the transfer and user to transfer to
        self.account_balance -= amount # the transferring user's account decreases by the transfer amount
        other_user.account_balance += amount # the other user's account increases by the transfer amount

lydia = User("Lydia", "lydia@fofo.com")
fayez = User("Fayez", "Fayez@bcs.com")
karim = User("Karim", "Karim@Apeak.com")

lydia.make_deposit(100)
lydia.make_deposit(500)
lydia.make_deposit(50)
lydia.make_withdrawal(250)
lydia.display_user_balance()

fayez.make_deposit(1000)
fayez.make_deposit(250)
fayez.make_withdrawal(600)
fayez.make_withdrawal(600)
fayez.display_user_balance()

karim.make_deposit(200)
karim.make_withdrawal(20)
karim.make_withdrawal(75)
karim.make_withdrawal(13)
karim.display_user_balance()

lydia.transer_money(karim, 300)
lydia.display_user_balance()
karim.display_user_balance()
