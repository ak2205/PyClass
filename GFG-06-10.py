# 06-ARMSTRONG NUMBER

def power(x, y):
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)

    return x * power(x, y // 2) * power(x, y // 2)

def order(x):
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10
    return n

def isArmstrong(x):
    n = order(x)
    temp = x
    sum1 = 0
    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + power(r, n)
        temp = temp // 10
    return (sum1 == x)

x = 991
print(isArmstrong(x))

x = 2751
print(isArmstrong(x))

# 07-AREA-OF-CIRCLE

pi = 3.14
r = float(input("Enter value of radius"))
h = float(input("Enter the height"))

area_circle = int(pi * r * r)
print("Area of a circle =", area_circle)

perimeter = int(2 * pi * r)
print("Perimeter of circle is = ", perimeter)

vol_cone = int(0.33 * pi * r * r * h)
print("Volume of a cone is =", vol_cone)


# 08-ALL-PRIME-INTERVALS

def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i / 2) + 1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list


starting_range = 2
ending_range = 7
lst = prime(starting_range, ending_range)
if len(lst) == 0:
    print("\nThere are no prime numbers in this range")
else:
    print("\nThe prime numbers in this range are: ", lst)

# 09-PRIME OR NOT

num = 77

if num > 1:
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")
    else:
        print(num, "\t\n is not a prime number")

# Optimized Method
from math import sqrt

n = 1
prime_flag = 0
if (n > 1):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            prime_flag = 1
            break
        if (prime_flag == 0):
            print("true")
        else:
            print("false")
else:
    print("false")

# 10-FIBONACCI

# With Recursion

def Fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
print(Fibonacci(11))

# With Dynamic Programming

FibArray = [0, 1]
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
        FibArray.append(temp_fib)
        return temp_fib
print(fibonacci(8))

# Dynamic Programming with Space Optimization

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b
print(fibonacci(7))
