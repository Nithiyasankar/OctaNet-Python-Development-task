import time

print("Please insert Your CARD...")

# Simulating card processing time
time.sleep(3)

# Predefined ATM pin and initial balance
PASSWORD = 1234
balance = 500000
attempts = 3  # Limit incorrect attempts

# Taking ATM pin from the user
while attempts > 0:
    try:
        pin = int(input("Enter your ATM PIN: "))
    except ValueError:
        print("Invalid input! Please enter a numeric PIN.")
        continue

    # Checking if PIN is correct
    if pin == PASSWORD:
        print("Login Successful!\n")
        while True:
            # Displaying ATM options to user
            print("""
                1 == Check Balance
                2 == Withdraw Money
                3 == Deposit Money
                4 == Exit
            """)

            try:
                # Taking option from user
                option = int(input("Please enter your choice: "))
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 4.")
                continue

            # Check Balance
            if option == 1:
                print(f"Your current balance is: {balance}")

            # Withdraw Money
            elif option == 2:
                try:
                    withdraw_amount = int(input("Enter amount to withdraw: "))
                    if withdraw_amount > balance:
                        print("Insufficient balance! Please enter a valid amount.")
                    elif withdraw_amount <= 0:
                        print("Invalid amount! Enter a positive value.")
                    else:
                        balance -= withdraw_amount
                        print(f"{withdraw_amount} has been debited from your account.")
                        print(f"Your updated balance is: {balance}")
                except ValueError:
                    print("Invalid input! Please enter a valid number.")

            # Deposit Money
            elif option == 3:
                try:
                    deposit_amount = int(input("Enter amount to deposit: "))
                    if deposit_amount <= 0:
                        print("Invalid amount! Enter a positive value.")
                    else:
                        balance += deposit_amount
                        print(f"{deposit_amount} has been credited to your account.")
                        print(f"Your updated balance is: {balance}")
                except ValueError:
                    print("Invalid input! Please enter a valid number.")

            # Exit ATM
            elif option == 4:
                print("Thank you for using our ATM! Have a great day!")
                break

            # Invalid Option Handling
            else:
                print("Invalid choice! Please enter a number between 1 and 4.")

        break  # Exit the PIN loop once authenticated

    else:
        attempts -= 1
        if attempts == 0:
            print("Too many incorrect attempts! Your card is blocked.")
        else:
            print(f"Wrong PIN! You have {attempts} attempts left. Please try again.")
