# 01-BASIC PYTHON ADDITION

num1 = 15
num2 = 12
sum = num1 + num2
print("Sum of {0} and {1} is {2}".format(num1, num2, sum))

# Example 2: Adding two number provided by user input using float

number1 = input("First number: ")
number2 = input("\nSecond number: ")
sum = float(number1) + float(number2)
print("The sum of {0} and {1} is {2}".format(number1, number2, sum))


# 02-MAXIMUM OF TWO NUMBERS
# using "if-else" statement

def maximum(a, b):
    if a >= b:
        return a
    else:
        return b


a = 2
b = 4
print(maximum(a, b))

# Using max() function

a = 2
b = 4
maximum = max(a, b)
print(maximum)

# Using Ternary Operator

a = 2
b = 4
print(a if a >= b else b)


# 03-Factorial of a Number
# RECURSIVE METHOD

def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);


num = 5;
print("Factorial of", num, "is",
      factorial(num))


# ITERATIVE METHOD

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
    while (n > 1):
        fact *= n
        n -= 1
        return fact


num = 5;
print("Factorial of", num, "is",
      factorial(num))


# Using Ternary Operator

def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


num = 5
print("Factorial of", num, "is",
      factorial(num))

# Using Built-in Function

import math


def factorial(n):
    return (math.factorial(n))


num = 5
print("Factorial of", num, "is", factorial(num))


# 04-SIMPLE-INTEREST

def simple_interest(p, t, r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)
    si = (p * t * r) / 100

    print('The Simple Interest is', si)
    return si


simple_interest(8, 6, 8)


# 05-COMPOUND-INTEREST

def compound_interest(principle, rate, time):
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", CI)

compound_interest(75000, 9.75, 5)
