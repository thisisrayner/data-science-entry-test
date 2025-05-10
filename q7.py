# q7.py
# Problem: Objects / Classes - Simple Bank Account
# Create a Python class named `BankAccount`.
# The class should have:
# 1. An `__init__` method that initializes an account with an `account_holder_name` (string)
#    and an initial `balance` (float, defaults to 0.0).
# 2. A `deposit` method that takes an `amount` and adds it to the balance.
#    It should print a message confirming the deposit.
# 3. A `withdraw` method that takes an `amount` and subtracts it from the balance.
#    It should check for sufficient funds. If funds are insufficient, print an error message.
#    Otherwise, print a confirmation message.
# 4. A `get_balance` method that returns the current balance.
# 5. A `display_account_info` method that prints the account holder's name and current balance.

class BankAccount:
    """
    A simple class to represent a bank account.
    """

    def __init__(self, account_holder_name, initial_balance=0.0):
        """
        Initializes a new BankAccount object.

        Args:
            account_holder_name (str): The name of the account holder.
            initial_balance (float, optional): The starting balance. Defaults to 0.0.
        """
        if not isinstance(account_holder_name, str) or not account_holder_name.strip():
            raise ValueError("Account holder name must be a non-empty string.")
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")

        self.account_holder_name = account_holder_name
        self.balance = float(initial_balance) # Ensure balance is float
        print(f"Account created for {self.account_holder_name} with initial balance: ${self.balance:.2f}")

    def deposit(self, amount):
        """
        Deposits a given amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Invalid deposit amount. Amount must be positive.")
            return

        self.balance += float(amount)
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraws a given amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw. Must be positive.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Invalid withdrawal amount. Amount must be positive.")
            return

        if amount > self.balance:
            print(f"Insufficient funds for withdrawal of ${amount:.2f}. Current balance: ${self.balance:.2f}")
        else:
            self.balance -= float(amount)
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_balance(self):
        """
        Returns the current account balance.

        Returns:
            float: The current balance.
        """
        return self.balance

    def display_account_info(self):
        """
        Prints the account holder's name and current balance.
        """
        print(f"\n--- Account Information ---")
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Current Balance: ${self.balance:.2f}")
        print(f"---------------------------")


if __name__ == "__main__":
    print("--- Bank Account Management ---")

    # Create an account
    try:
        account1 = BankAccount("Alice Wonderland", 100.0)
        account1.display_account_info()

        # Perform operations
        account1.deposit(50.75)
        account1.withdraw(30)
        account1.display_account_info()

        account1.withdraw(200) # Attempt to overdraw
        account1.deposit(-10)  # Attempt invalid deposit
        account1.withdraw(0)   # Attempt invalid withdrawal
        account1.display_account_info()

        print("\nCreating another account with default balance:")
        account2 = BankAccount("Bob The Builder")
        account2.display_account_info()
        account2.deposit(1000)
        current_bal_bob = account2.get_balance()
        print(f"Bob's current balance retrieved via get_balance(): ${current_bal_bob:.2f}")
        account2.display_account_info()

        print("\nTesting invalid account creation:")
        try:
            invalid_account1 = BankAccount("", 100)
        except ValueError as e:
            print(f"Error creating account: {e}")

        try:
            invalid_account2 = BankAccount("Charlie", -50)
        except ValueError as e:
            print(f"Error creating account: {e}")

    except ValueError as e:
        print(f"An error occurred during account setup: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Test Scenarios:
# 1. Create account, deposit, withdraw (valid), display.
#    - Expected: Balances update correctly, messages are printed.
# 2. Attempt to withdraw more than balance.
#    - Expected: "Insufficient funds" message, balance unchanged.
# 3. Attempt to deposit/withdraw negative or zero amount.
#    - Expected: "Invalid amount" message, balance unchanged.
# 4. Create account with default (zero) balance.
#    - Expected: Initial balance is 0.0.
# 5. Use get_balance() method.
#    - Expected: Returns correct float value.
# 6. Test invalid initializations (e.g., empty name, negative initial balance).
#    - Expected: ValueError raised.
