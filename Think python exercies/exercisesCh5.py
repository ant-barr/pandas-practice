# In this chapter, we saw ways to write an if statment with three branches, using a chained conditional or 
# a nested conditional. 

"""
Exercise 1:
The time module provides a function called time, that returns the number of seconds since the
"unix epoch," which is january 1, 1970, 00:00:00 UTC
(Coordinated Universal Time):
"""
from time import time
now = time()
print(now)

"""
Use floor division and the modulus operator to compute the number
of days since January 1, 1970, and the current time of day in hours, minutes, and seconds
"""

days = now // 86400
seconds_today = now % 86400
hours = (seconds_today // 3600)
minutes = (seconds_today % 3600) // 60
seconds = seconds_today % 60

print("Days since Unix Epoch: ", int(days))
print("Time of day: ", int(hours),":",int(minutes),":", int(seconds))
print()

"""
Exercise 2
if you are given three sticks, you may or may not be able to arrange them in a triange. 
for example, if one of the sticks is 12 inches long and the other two are 1 inch long
you will not be able to get the short sticks to meet in the middle. for any three lengths there
is a test to see if it is possible to form a triangle
    if any of the three lengths is greater than the sum of the other two, than you CANNOT
    form a triange. otherwise you can.

write a function named is_triangle that takes three integers as arguments, and prints
yes or no depending on whether or not you can form a triangle from the sticks with the given lenghts
    Hing: use a chained conditional
"""
def is_triangle(l1, l2, l3):
    if l1 + l2 > l3 and l3 + l2 > l1 and l1 + l3 > l2:
        print("Yes, the sticks can form a triangle!")
    else:
        print("No, the three sticks cannot form a triangle.")

print("triangle condition 1")
is_triangle(3, 4, 13)
is_triangle(3, 4, 6)
print()

print("triangle condition 2")
is_triangle(14, 4, 5)
is_triangle(14, 9, 9)
print()

print("triangle condition 3")
is_triangle(3, 16, 7)
is_triangle(4, 23, 20)
print()

"""
Exersies 2
"""

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        print(n, s)
        recurse(n-1, n+s)
        

recurse(3, 0)

"""
Stack Diagram

recurse  n ==> 3,  s ==> 3 + 0 = 3
recurse  n ==> 2,  s ==> 2 + 3 = 5
recurse  n ==> 1,  s ==> 1 + 5 = 6
print(s) s ==> 6
"""

"""
Exercise 3
read the following function and see if you can figure out what it does, 
then run it and see if you got it right. Adjust the values of length, angle, and factor
and see what effect they have on the result
"""
# %%
from jupyturtle import make_turtle, forward, left, right, back

def draw(length):
    angle = 50
    factor = 0.6
    if length > 5:
        forward(length)
        left(angle)
        draw(factor * length)
        right(2 * angle)
        draw(factor * length)
        left(angle)
        back(length)

make_turtle(delay = 0.02)
draw(50)

"""
What do I think it does:
I see it calls itself and multiplies the length by the factor,
which will reduce the size of length,
I think it will draw a spiral, just making a guess.
it actually makes a fractal shape., I should have infered this because
the function is recursive and once it has gone through the recursion, it goes back to a starting point

"""
# %%
'''
Exercise 4:
Draw a Koch curve with length x, doing these:
    1. Draw a Koch curve with length x/3
    2. Turn left 60 degrees
    3. Draw a Koch curve with length x/3
    4. Turn right 120 Degrees
    5. Draw a koch curve with length x/3
    6. Turn left 60 degrees
    7. Draw a Koch curve with length x/3

    The exception is if x is less than 5, in that case you can just draw a straight line
    with length x

    Write a function called koch that takes x as a parameter and draws a koch curve with the given 
    length. the result should look like this
'''

def koch(x):
    if x < 5:
        forward(x)
    else:
        koch(x/3)
        left(60)
        koch(x/3)
        right(120)
        koch(x/3)
        left(60)
        koch(x/3)
    


make_turtle(delay = 0.02)
koch(500)
# %%
'''
this is me practising vim motions '''
#going to add a cell using the '#%%'
import random
num_list = [3, 4, 5, 6]
print("list before shuffle: ", num_list)
random.shuffle(num_list)
print("List after shuffle: ", num_list)

# %%