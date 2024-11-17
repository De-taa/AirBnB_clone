#!/usr/bin/python3

def fizzbuzz_plus():
    while True:
        # Step 1: Input Validation
        try:
            start = int(input("Enter the start number: "))
            end = int(input("Enter the end number: "))
            if start > end:
                print("Start number must be less than or equal to the end number. Please try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter valid integers.")
            continue

        # Step 2: FizzBuzz Logic
        print("\nFizzBuzz Results:")
        for num in range(start, end + 1):
            if num % 3 == 0 and num % 5 == 0:
                print("FizzBuzz")
            elif num % 3 == 0:
                print("Fizz")
            elif num % 5 == 0:
                print("Buzz")
            else:
                print(num)

        # Step 3: Repeat Option
        repeat = input("\nDo you want to run the program again? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("Goodbye!")
            break


# Run the program
fizzbuzz_plus()
