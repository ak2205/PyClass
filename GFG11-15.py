# 11-CHECK IF GIVEN NUMBER IS A FIBONACCI NUMBER

import math
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x

def isFibonacci(n):
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)

for i in range(1, 11):
    if (isFibonacci(i) == True):
        print(i, "is a Fibonacci Number")
    else:
        print(i, "is a not Fibonacci Number ")

# 12-N'\th MULTIPLE OF A NUMBER IN FIBONACCI SERIES

def findPosition(k, n):
    f1 = 0
    f2 = 1
    i = 2
    while i != 0:
        f3 = f1 + f2
        f1 = f2
        f2 = f3

        if f2 % k == 0:
            return n * i
        i += 1
    return
n = 5
k = 4
print("Position of n\'th multiple of k in Fibonacci Series is", findPosition(k, n))

# 13-ASCII Value of a character

c = 'g'
print("The ASCII value of '" + c + "' is", ord(c))

# 14- Sum of squares of first n natural numbers

# Using O(N)

def squaresum(n):
    sm = 0
    for i in range(1, n + 1):
        sm = sm + (i * i)
    return sm
n = 4
print(squaresum(n))

# Using O(1)

def squaresum(n):
    return (n * (n + 1) * (2 * n + 1)) // 6
n = 4
print(squaresum(n))

# Avoiding early overflow

def squaresum(n):
    return (n * (n + 1) / 2) * (2 * n + 1) / 3
n = 4
print(squaresum(n))


# 15-CUBE SUM OF FIRST N NATURAL NUMBERS

# Using O(N)

def sumOfSeries(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i * i
    return sum
n = 5
print(sumOfSeries(n))


# Using O(1)

def sumOfSeries(n):
    x = (n * (n + 1) / 2)
    return (int)(x * x)
n = 5
print(sumOfSeries(n))

#Avoid overflow

def sumOfSeries(n):
    x = 0
    if n % 2 == 0:
        x = (n / 2) * (n + 1)
    else:
        x = ((n + 1) / 2) * n
    return (int)(x * x)
n = 5
print(sumOfSeries(n))




