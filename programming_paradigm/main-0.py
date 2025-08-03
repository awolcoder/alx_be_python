import sys
from bank_account import BankAccount

def main():
    # Create a bank account instance with a starting balance of $100
    account = BankAccount(100)

    # Check if a command was passed through command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Extract command and optional amount (split by ':')
    command_parts = sys.argv[1].split(':')
    command = command_parts[0]  # e.g., deposit, withdraw, display
    amount = float(command_parts[1]) if len(command_parts) > 1 else None

    # Process commands
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

# Run the program
if __name__ == "__main__":
    main()
