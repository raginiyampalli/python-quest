import HelperFunctions
def fibonacci_series(target, num1, num2, series):
    if target == 0:
        series.append(num1 + num2)
    else:
        series.append(num1 + num2)
        fibonacci_series(target - 1, num2, num1 + num2, series)


"""Testing above function"""
series = list()
fibonacci_series(5, 0, 1, series)

HelperFunctions.print_numbers(series)
