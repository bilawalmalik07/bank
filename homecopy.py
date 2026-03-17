import sys


account_balance = 0
account_opened = False


def open_account():
    global account_balance, account_opened, name
    name = input("What's your name: ").capitalize()
    print(f'Heyyy! Welcome {name}.\n')
    print(f'You must deposit $20 or more to create an account.\n')
    while True:
        consent = input("Do you want to create an account? [yes/no]: ").lower()
        if consent in ["yes", "no"]:
            break
        print("Please type yes or no.")
    if consent == "yes":
        while True:
            try:
                print(f"Lets create a 4-digit pin first [eg: 1234].")
                pin = input("Enter a pin : ")
                while not (pin.isdigit()) and not (len(pin) == 4):
                    print("A four digit pin please [eg 1234]")
                    pin = input("Enter a pin : ")
                print("Pin created.")
                initial_deposit = float(
                    input("How much would you like to deposit: "))

                if initial_deposit < 20:
                    print("Error: Minimum deposit is $20. Please try again.")
                    continue
                account_balance += initial_deposit
                account_opened = True
                print(f'Congratulations {name}! Your account is created.')
                print(f'Current balance: ${account_balance:,.2f}')
                break
            except ValueError:
                print("Invalid input. Please enter a number (e.g., 20 or 25.75).")
    else:
        exit()


def deposit():
    global account_balance
    while True:
        try:
            user_input = input("Enter the amount you want to deposit: ")
            amount = float(user_input)

            if amount <= 0:
                print("Please enter an amount greater than 0.")
                continue

            account_balance += amount
            print(
                f'Deposit successful. Current balance: ${account_balance:,.2f}')
            break

        except ValueError:
            print("Invalid input. Please use numbers (e.g., 50 or 90.75).")


def withdraw():
    global account_balance
    while True:
        try:
            withdrawal = float(
                input("Enter the amount you want to withdraw: "))
            if withdrawal > account_balance:
                print("Request Declined: Insufficent balance")
                print(f"Your account balance is {account_balance:,.2f}.")
                ask = input(
                    "You want to withdraw a different amount? [yes/no]")
                while ask not in ["yes", "no"]:
                    ask = input(
                        "You want to withdraw a different amount? [yes/no]")
                if ask == "yes":
                    continue
                else:
                    return
            if withdrawal <= 0:
                print("Please enter a positive amount.")
                continue
            account_balance -= withdrawal
            print(
                f'Withdrawal successful. Your remaining balance: ${account_balance:,.2f}')
            break
        except ValueError:
            print("Invalid input. Please use numbers (e.g., 50 or 90.75).")


def print_balance():
    global account_balance
    print(f'Current balance = ${account_balance:,.2f}')


def exit_program():
    print("bye have a good day.")
    sys.exit()


def ask():
    print(f"{'-'*40}")
    print(f'What would you like to do {name}.')
    print("OPTIONS")
    print("1) Menu for [Deposit , Withdraw , Check balance]")
    print("2) Exit")
    asking = input("Choose [1 or 2] :")
    if asking not in ["1", "2"]:
        asking = input("Please Choose [1 or 2] :")
    else:
        exit_program()
    if asking == "1":
        print(f"{'-'*40}")
        print("OPTIONS")
        print("1) Deposit")
        print("2) Withdraw")
        print("3) Check balance")
        print("4) Exit")
        menu_choice = input(f'{name}. Choose [1 , 2 , 3 or 4]: ')
        if menu_choice not in ["1", "2", "3", "4"]:
            menu_choice = input(f'{name}.Please Choose [1 , 2 , 3 or 4]: ')
        if menu_choice == "1":
            deposit()
        elif menu_choice == "2":
            withdraw()
        elif menu_choice == "3":
            print_balance()
        else:
            exit_program()


def main():
    print(f"{'-'*40}")
    print(f"{'-'*40}")
    print(f"{'-'*11}CLI BANKING SYSTEM{'-'*11}")
    print(f"{'-'*40}")
    print(f"{'-'*40}")
    print("OPTIONS")
    print("1) Create a new account")
    print("2) Sign into existing account")
    print("3) Exit")
    selection = input("Choose [1 , 2 or 3] :")
    while selection not in ["1", "2", "3"]:
        selection = input("Please Choose [1 , 2 or 3] :")
    if selection == "1":
        open_account()
        ask()
    elif selection == "2":
        pass
    else:
        exit()


if __name__ == "__main__":
    main()
