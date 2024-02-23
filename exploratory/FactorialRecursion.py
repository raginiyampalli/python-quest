def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)


"""Testing above function"""

print(factorial(3))
