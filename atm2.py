class ATM:
    def __init__(self):
        self.balance = 5000  # Initial balance
        self.pin = "1234"    # Simple PIN system
        self.authenticated = False

    def authenticate(self):
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:
            print("Authentication successful.\n")
            self.authenticated = True
        else:
            print("Incorrect PIN. Access denied.\n")
            self.authenticated = False

    def check_balance(self):
        if self.authenticated:
            print(f"Your current balance is ₹{self.balance}\n")
        else:
            print("Please authenticate first.\n")

    def deposit(self):
        if self.authenticated:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                self.balance += amount
                print(f"₹{amount} deposited successfully.")
                self.check_balance()
            else:
                print("Enter a valid amount.\n")
        else:
            print("Please authenticate first.\n")

    def withdraw(self):
        if self.authenticated:
            amount = float(input("Enter amount to withdraw: ₹"))
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"₹{amount} withdrawn successfully.")
                self.check_balance()
            else:
                print("Insufficient balance or invalid amount.\n")
        else:
            print("Please authenticate first.\n")

# ------------------ Main Program ------------------ #
atm = ATM()

while True:
    print("==== ATM Menu ====")
    print("1. Authenticate")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")
    
    choice = input("Select an option: ")

    if choice == '1':
        atm.authenticate()
    elif choice == '2':
        atm.check_balance()
    elif choice == '3':
        atm.deposit()
    elif choice == '4':
        atm.withdraw()
    elif choice == '5':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid option. Try again.\n")
