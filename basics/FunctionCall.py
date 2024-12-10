
# This program demonstrates function call in Python

def addNumbers(num1: int, num2: int) -> int:
    """ Add 2 numbers """
    sum = num1 + num2
    return sum

num1 = 10
num2 = 25

# Call another function to add above 2 numbers
sum = addNumbers(num1, num2)

# print sum 
print('o/p from Function call - Sum of {0} and {1} is {2}'.format(num1, num2, sum))


