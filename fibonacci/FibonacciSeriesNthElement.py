
# This program shall compute Nth element of Fibonacci series

def fibonacciValue(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacciValue(n-1) + fibonacciValue(n-2)

num = 10
fibVal = fibonacciValue(num)
print('{0} element of Fibonacci series = {1}'.format(num, fibVal))




