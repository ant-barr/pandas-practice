

def sum_to(n):
    if n == 0:
        return 0
    print(n) 
    return n + sum_to(n-1)

print(sum_to(3))

# write a function square_area(side) that returns
# the area of a square

def square_area(side):
    return side * 4

#15 write a generalized function polygon_perimeter(n, length)
# that computes the perimeter of a regular n sided polygon

def polygon_perimeter(n, length):
    perimeter = length * n
    print(perimeter)

# 16 write a recursive function factorial(n) that returns
# the factorial of a number

def factorial(n):
    if n == 0:
        return 0
    return n * factorial(n-1)

# 17 write a function is_prime(n) that returns true if n is prime
# false otherwise
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True 
            

print(is_prime(9973))

def fibonacci(n):
    if n <= 0:
        return
    a = 0
    b = 1
    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c

fibonacci(10)