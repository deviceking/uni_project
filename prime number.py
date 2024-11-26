user_input = int(input("Enter a number: "))

store = []

if user_input > 1:
    divisor = 2  # Start with the smallest prime
    while user_input > 1:
        if user_input % divisor == 0:
            store.append(divisor)  # Add the prime factor
            user_input //= divisor  # Reduce the number
        else:
            divisor += 1  # Move to the next potential divisor
else:
    print("Error: Enter a number greater than 1.")

if store:
    print("Prime factors:", store)
