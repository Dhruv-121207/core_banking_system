from bank import (
    Bank,
    SavingsAccount,
    CheckingAccount,
    AccountNotFoundError,
    InsufficientBalanceError,
    InvalidAmountError
)

def show_menu():
    print("\n" + "=" * 30)
    print("         PYTHON BANK")
    print("=" * 30)
    print("1. Create account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Transfer money")
    print("5. Check balance")
    print("6. View transactions")
    print("7. Check Overdraft Amount")
    print("0. Exit")


def create_account(bank):
    name = input("Enter account holder name: ").strip()

    print("Select account type")
    print("1. Savings account")
    print("2. Checking account")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        account = SavingsAccount(name)
    elif choice == "2":
        account = CheckingAccount(name)
    else:
        print("Invalid account type")
        return

    bank.add_accounts(account)
    print("Account created successfully")
    print("Account number:", account.acc_num)


def main():
    bank = Bank("My Bank")

    while True:
        show_menu()
        choice = input("Enter option: ").strip()

        try:
            if choice == "1":
                create_account(bank)

            elif choice == "2":
                acc_num = int(input("Enter account number: "))
                amount = float(input("Enter amount: "))

                account = bank.get_account(acc_num)
                if not account:
                    raise AccountNotFoundError("Account not found")

                account.deposit(amount)
                print("Deposit successful")

            elif choice == "3":
                acc_num = int(input("Enter account number: "))
                amount = float(input("Enter amount: "))

                account = bank.get_account(acc_num)
                if not account:
                    raise AccountNotFoundError("Account not found")

                account.withdraw(amount)
                print("Withdrawal successful")

            elif choice == "4":
                from_acc = int(input("From account number: "))
                to_acc = int(input("To account number: "))
                amount = float(input("Enter amount: "))

                bank.transfer(from_acc, to_acc, amount)
                print("Transfer successful")

            elif choice == "5":
                acc_num = int(input("Enter account number: "))

                account = bank.get_account(acc_num)
                if not account:
                    raise AccountNotFoundError("Account not found")

                print(account.check_balance())

            elif choice == "6":
                acc_num = int(input("Enter account number: "))

                account = bank.get_account(acc_num)
                if not account:
                    raise AccountNotFoundError("Account not found")

                transactions = account.display_transactions()
                if not transactions:
                    print("No transactions found")
                else:
                    for t in transactions:
                        print(t)
            
            elif choice == "7":
                acc_num = int(input("Enter account number: "))

                account = bank.get_account(acc_num)
                if not account:
                    raise AccountNotFoundError("Account not found")

                if not isinstance(account, CheckingAccount):
                    print("Overdraft is only available for Checking Accounts")
                else:
                    print(account.display_overdraft())

            elif choice == "0":
                print("Exiting program")
                break

            else:
                print("Invalid option")

        except (InvalidAmountError, InsufficientBalanceError, AccountNotFoundError) as e:
            print("Error:", e)

        except ValueError:
            print("Invalid input")


if __name__ == "__main__":
    main()
