import os
import sys
import psycopg2
from dotenv import load_dotenv

# Try loading the file, but don't crash if it's missing (it's missing on GitHub!)
load_dotenv("database.env")

# This will get the URL from the JSON if the file above wasn't found
connection_url = os.getenv("DATABASE_URL")

if not connection_url:
    print("❌ ERROR: DATABASE_URL is empty in the environment.")
    sys.exit()

try:
    conn = psycopg2.connect(connection_url)
    print("✅ Success! Database connected.")
except Exception as e:
    print(f"❌ Connection failed: {e}")


balance = 0
account_opened = False


def open_account():
    global balance, account_opened, name, username
    name = input("\nWhat's your name: ").capitalize()
    print(f'\nHeyyy! Welcome {name}.\n')
    print(f'You must deposit $20 or more to create an account.\n')
    while True:
        consent = input("Do you want to create an account? [yes/no]: ").lower()
        if consent in ["yes", "no"]:
            break
        print("\nPlease type yes or no.\n")
    if consent == "yes":
        while True:
            try:
                username = input("\nCreate a username : ")
                cur = conn.cursor()
                sql_1 = "SELECT username from accounts WHERE username=%s"
                data_1 = (username,)
                cur.execute(sql_1, data_1)
                existing_user = cur.fetchone()
                if existing_user:
                    print("\nSorry! , this username is taken try another one.")
                    cur.close()
                    continue
                else:
                    print("\nUsername created")
                print(f"\nNow create a 4-digit Pin [eg: 1234].")
                pin = input("\nEnter a pin : ")
                while not (pin.isdigit()) or not (len(pin) == 4):
                    print("\nA four digit pin please [eg 1234]")
                    pin = input("\nEnter a pin : ")
                print("\nPin created.")
                initial_deposit = float(
                    input("\nHow much would you like to deposit: "))

                if initial_deposit < 20:
                    print("\nError: Minimum deposit is $20. Please try again.")
                    continue
                balance += initial_deposit
                account_opened = True
                try:
                    cur = conn.cursor()
                    sql_2 = "INSERT INTO accounts (name, username, pin, balance) VALUES (%s, %s, %s, %s);"
                    data_2 = (name, username, pin, initial_deposit)
                    cur.execute(sql_2, data_2)
                    conn.commit()
                    cur.close()
                except Exception as e:
                    print(f"\nFailed to save account: {e}")
                    conn.rollback()

                print(f'\nCongratulations {name}! Your account is created.')
                print(f'\nCurrent balance: ${balance:,.2f}')
                break
            except ValueError:
                print("\nInvalid input. Please enter a number (e.g., 20 or 25.75).")
    else:
        print("Returning back")
        return


def signin():
    global balance, account_opened, name, username
    account_opened = False
    login_name = input("\nEnter your username: ")
    login_pin = input("\nEnter your pin: ")

    try:
        cur = conn.cursor()
        sql_3 = "SELECT name, balance FROM accounts WHERE username = %s AND pin = %s"
        data_3 = (login_name, login_pin)
        cur.execute(sql_3, data_3)
        result = cur.fetchone()
        if result:
            name = result[0]
            balance = float(result[1])
            username = login_name
            account_opened = True
            print(f"\nLogin successful! Welcome back, {name}.")
            print(f"\nAccount Balance: ${balance:,.2f}")
            cur.close()
        else:
            print("\nInvalid username or pin. Please try again.")
            cur.close()
            return
    except Exception as e:
        print(f"\nDatabase error: {e}")


def deposit():
    global balance
    while True:
        try:
            user_input = input("\nEnter the amount you want to deposit: ")
            amount = float(user_input)

            if amount <= 0:
                print("\nPlease enter an amount greater than 0.")
                continue

            balance += amount
            try:
                cur = conn.cursor()
                sql_4 = "UPDATE accounts SET balance = %s WHERE username = %s"
                data_4 = (balance, username)
                cur.execute(sql_4, data_4)
                conn.commit()
                cur.close()
                break
            except Exception as e:
                print(f"\nFailed to save account: {e}")
                conn.rollback()

            print(
                f'\nDeposit successful. Current balance: ${balance:,.2f}')
            break

        except ValueError:
            print("\nInvalid input. Please use numbers (e.g., 50 or 90.75).")


def withdraw():
    global balance, username, name
    while True:
        try:
            withdrawal = float(
                input("\nEnter the amount you want to withdraw: "))
            if withdrawal > balance:
                print("\nRequest Declined: Insufficent balance")
                print(f"\nYour account balance is {balance:,.2f}.")
                ask = input(
                    "\nYou want to withdraw a different amount? [yes/no]")
                while ask not in ["yes", "no"]:
                    ask = input(
                        "\nYou want to withdraw a different amount? [yes/no]")
                if ask == "yes":
                    continue
                else:
                    return
            if withdrawal <= 0:
                print("\nPlease enter a positive amount.")
                continue
            balance -= withdrawal
            try:
                cur = conn.cursor()
                sql_5 = "UPDATE accounts SET balance = %s WHERE username = %s"
                data_5 = (balance, username)
                cur.execute(sql_5, data_5)
                conn.commit()
                cur.close()
                print(
                    f"\nWithdrawal successful. Your remaining balance = ${balance:,.2f}")
                break
            except Exception as e:
                print(f"\nFailed to save account: {e}")
                conn.rollback()
        except ValueError:
            print("\nInvalid input. Please use numbers (e.g., 50 or 90.75).")


def print_balance():
    global balance
    print(f'\nCurrent balance = ${balance:,.2f}')


def exit_program():
    print("\nbye have a good day.")
    sys.exit()


def ask():
    while True:
        print(f"{'-'*40}")
        print(f'What would you like to do {name}.')
        print("OPTIONS\n")
        print("1) Menu for [Deposit, Withdraw, Check balance]")
        print("2) Exit")

        asking = input("\nChoose [1 or 2] : ")
        while asking not in ["1", "2"]:
            asking = input("Please Choose [1 or 2] :")

        if asking == "2":
            exit_program()

        print(f"{'-'*40}")
        print("OPTIONS\n")
        print("1) Deposit")
        print("2) Withdraw")
        print("3) Check balance")
        print("4) Exit")

        menu_choice = input(f'{name}. Choose [1, 2, 3 or 4]: ')
        while menu_choice not in ["1", "2", "3", "4"]:
            menu_choice = input(f'{name}. Please Choose [1, 2, 3 or 4]: ')

        if menu_choice == "1":
            deposit()
        elif menu_choice == "2":
            withdraw()
        elif menu_choice == "3":
            print_balance()
        else:
            exit_program()


def main():
    while True:
        print(f"{'-'*40}")
        print(f"{'-'*40}")
        print(f"{'-'*11}CLI BANKING SYSTEM{'-'*11}")
        print(f"{'-'*40}")
        print(f"{'-'*40}")
        print("OPTIONS\n")
        print("1) Create a new account")
        print("2) Sign into existing account")
        print("3) Exit")
        print(f"{'-'*40}")
        selection = input("Choose [1 , 2 or 3] : ")
        while selection not in ["1", "2", "3"]:
            selection = input("\nPlease Choose [1 , 2 or 3] : ")
        if selection == "1":
            open_account()
            if account_opened:
                ask()
        elif selection == "2":
            signin()
            if account_opened:
                ask()
        else:
            exit_program()


if __name__ == "__main__":
    main()
