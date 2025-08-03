class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account.
        :param initial_balance: Optional starting balance, defaults to 0.
        """
        self.__account_balance = initial_balance  # Private attribute for encapsulation

    def deposit(self, amount):
        """
        Deposit money into the account.
        :param amount: Positive float value to deposit.
        """
        if amount > 0:
            self.__account_balance += amount  # Increase balance
        else:
            print("Deposit amount must be positive.")  # Validation check

    def withdraw(self, amount):
        """
         Withdraw money if sufficient funds are available.
        :param amount: Positive float value to withdraw.
        :return: True if withdrawal is successful, False otherwise.
        """
        if amount > 0:
            if self.__account_balance >= amount:  # Check if enough balance exists
                self.__account_balance -= amount  # Deduct balance
                return True
            else:
                return False # Insufficient funds
        else:
            print("Withdraw amount must be positive.")  # Validation check
            return False
        
    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance}")
