import sys
account_balance = 0
account_opened = False


def open_account():
    global account_balance, account_opened, name
    name = input("Whats your name: ").capitalize()
    print(f'Heyyy! welcome {name}.\n')
    print(f'You would have to deposit 20$ or more to create an account.\n')
    consent = input("You want to create? [yes/no] :").lower()
    while consent not in ["yes", "no"]:
        try:
            name = input("Whats your name: ").capitalize()
            print(f'Heyyy! welcome {name}.\n')
            print(f'You would have to deposit 20$ or more to create an account.\n')
            consent = input("You want to create? [yes/no] :").lower()
            consent = input("You want to create? please [yes/no] :").lower()
            break
        except:
            print("no")
    while consent == "yes":
        try:
            intial_deposit = float(
                input("How much would you like to deposit: "))
            account_balance += intial_deposit
            account_opened = True
            print(
                f'Congratulations {name}.\n'
                f'Your account is created.\n'
                f'Your current balance: ${account_balance:,.2f}')
        except:
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
    withdrawl = float(input("Enter the amount you want to withdraw: "))
    account_balance -= withdrawl
    print(
        f'Withdrawal successful. Your current balance: ${account_balance:,.2f}')


def print_balance():
    global account_balance
    print(f'Current balance= ${account_balance:,.2f}')


def exit():
    print("bye have a good day.")
    sys.exit()


def ask():
    print("------------------------------------------------------------------------")
    print(f'What would you like to do {name}.')
    print("OPTIONS")
    print("1) Menu for [Deposit , Withdraw , Check balance]")
    print("2) Exit")
    asking = input("Choose [1 or 2] :")
    if asking not in ["1", "2"]:
        asking = input("Please Choose [1 or 2] :")
    else:
        exit()
    if asking == "1":
        print("------------------------------------------------------------------------")
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
            exit()


def main():
    print("------------------------------------------------------------------------")
    print("------------------------------------------------------------------------")
    print("-------------------------CLI BANKING SYSTEM-----------------------------")
    print("------------------------------------------------------------------------")
    print("------------------------------------------------------------------------")
    print("OPTIONS")
    print("1) Create a new account")
    print("2) Sign into existing account")
    print("3) Exit")
    selection = input("Choose [1 , 2 or 3] :")
    if selection not in ["1", "2", "3"]:
        selection = input("Please Choose [1 , 2 or 3] :")
    if selection == "1":
        open_account()
    elif selection == "2":
        pass
    else:
        exit()


if __name__ == "__main__":
    main()
