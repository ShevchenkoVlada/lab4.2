def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_power_of_2(number):
     return (number != 0) and ((number & (number - 1)) == 0)

def is_power_of_5(number):
    return (number != 0) and ((number & (number - 1)) == 0) and (number & 0x55555555 == number)
