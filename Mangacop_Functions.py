def smallest_factor(n):
    if n == 2:
        return n
    if n % 2 == 0:
        return 2
    max_div = int(n ** 0.5)
    for d in range(3, 1 + max_div, 2):
        if n % d == 0:
            return d
    return n


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def display_primes(start, end):
    if start < 0:
        print("Enter a non-negative number.")
        return
    if end <= start:
        print(f"Enter a number greater than {start}.")
        return

    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)


def find_factor(n):
    if n < 0:
        print("Enter a non-negative number.")
        return

    print(f"The smallest factor of {n} is {smallest_factor(n)}.")


while True:
    print("Select an option:")
    print("1. Find the smallest factor of a number.")
    print("2. Find the prime numbers of a range.")
    print("0. Exit.")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        print("Program terminated.")
        break
    elif choice == 1:
        n = int(input("Enter a number: "))
        find_factor(n)
    elif choice == 2:
        start = int(input("Enter a number [start]: "))
        end = int(input("Enter a number [end]: "))
        display_primes(start, end)
    else:
        print("Invalid choice. Please try again.")