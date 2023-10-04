def is_prime(num):
    if num <= 1:
        return False
    print(int(num**0.5) + 1)
    for i in range(2, int(num**0.5) + 1):
        print(i)
        if num % i == 0:
            return False
    return True


# Example usage
number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
