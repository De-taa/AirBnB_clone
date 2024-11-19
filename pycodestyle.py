#!/usr/bin/python3

# A simple code that saves money

# Initialize saving process
savings = 20000
print(f"My savings: #{savings:,}")

# Ask the user for the amount to deposit
deposit = int(input("Enter amount to deposit: #"))

# Add deposit to savings
savings += deposit
print(f"My savings: #{savings:,}")

# Ask the user if they'd like to deposit more
another = input("Would you like to make another deposit? (yes/no): ")

if another == "yes":
    # Ask the user for amount
    deposit = int(input("Enter amount to deposit: #"))

    # Add deposit to savings
    savings += deposit
    print(f"My savings: #{savings:,}")
else:
    print("Thank you for saving with us!")
