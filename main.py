def check_number():
    repeat = int(input("How many numbers do you want to check? "))
    for _ in range(repeat):
        num = float(input("Enter a number: "))
        if num > 0:
            print(f"{num} is a positive number.")
        elif num < 0:
            print(f"{num} is a negative number.")
        else:
            print(f"{num} is zero.")

# Example usage:
check_number()
