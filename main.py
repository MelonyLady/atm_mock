
import time

set_pin = "9999"


def pin():
    user_input = input("Please enter your 4 digit PIN: ")
    if user_input.isnumeric():
        pass
    else:
        print("A PIN is made of 4 numbers")
        raise Exception(TypeError)
    if len(user_input) != 4:
        print("PIN must be 4 digits in length")
        raise Exception("PIN must be 4 digits in length")
    return user_input


def pin_check():
    attempts = 0
    while attempts <= 3:
        time.sleep(1)

        if pin() == set_pin:
            print("---")
            user_selection()
            break

        elif attempts < 2:
            attempts += 1
            print(f"That was incorrect, please enter your pin again you have {3 - attempts} attempt(s) left")

        elif attempts := 3:
            print("I'm sorry, but we are unable to process your request at this time")
            break


def user_selection():
    balance = 100
    print()
    print("Welcome to Mountebank".center(100))
    print()
    while True:
        time.sleep(1)
        print("---")
        print("Please select an action below:")
        print("[1] Check your Current Balance")
        print("[2] Withdraw from your account")
        print("[3] Exit")
        action = input("Please enter the number of the action you would like to take: ")
        print()

        if action == '1':
            view_balance(balance)

        elif action == '2':
            print("Withdrawal Selected")
            try:
                balance = withdrawal(starting_balance=balance)
            except ValueError as error:
                print(error)

        elif action == '3':
            print()
            print("Thank you for banking with Mountebank".center(100))
            print("Goodbye!".center(100))
            break

        else:
            print("Sorry, that wasn't one of the options. Please try again.")


def withdrawal(starting_balance):
    try:
        withdrawal_amount = float(input("Please state the amount you wish to withdraw: "))
    except ValueError:
        raise ValueError("Please enter numeric amount. Thank you!")
    else:
        if float(withdrawal_amount) > starting_balance:
            raise Exception("That amount is more than the available amount")
        elif withdrawal_amount <= 0:
            raise ValueError("Enter only positive amounts, please!")
        else:
            updated_balance = starting_balance - withdrawal_amount
            print()
            print("*****Don't forget to take your money!******".center(100))
            print(f"You now have £{updated_balance:.2f} left in your account")
            print()
    return updated_balance


def view_balance(balance):
    print(f"You have £{balance:.2f} in your account.")


if __name__ == '__main__':
    pin_check()