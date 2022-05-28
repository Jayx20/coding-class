# there are functions built into python, the most basic of which help us do math

number = 1.5

# rounded should round up to 2

rounded_number = round('round 1.5', number)

print(rounded_number)

# ceil() and floor() also exist, but they are locked away in a 'module' called 'math'
# a module is a collection of code
# lets use math in our code

# this lets us use whatever is inside of math
import math

# then we type math and the function we want
# the . gets something inside of the math module

print('floor 1.5', math.floor(number))

number -= 0.4 # 1.5 - 0.4 = 1.1

print('ceil 1.1', math.ceil(number))

# please note the number stored inside of the variable named `number` is not changing unless I use the assignment operator = or something like += (addition assignment operator)

# here are the important arithmatic and assignment operators
num = 1 + 1 # addition
num = 1 - 1 # subtract
num = 1 * 1 # multiplication
num = 1 / 1 # division

# you can also add negative numbers, and multiply by decimals
num = 1 + -1  # same as 1 - 1
num = 1 * 0.5 # same as 1 / 2

# this operator is python-exclusive, but you can also use **, the exponent operator
# of course you can do this in other languages, but it's typewd differently 

num = 2 ** 2 # 2 to the power of 2, or 2^2

print('2**2', 2**2)

