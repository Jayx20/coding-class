
# Python is a dynamically typed language, which means it will not double check if you put the right type somewhere so you need to double check
# still, python does have types and sometimes you need to know them

# here's the simple python types:
# int     - integer, the most basic type of number
# float   - decimal number
# string  - characters
# boolean - can only be True or False (important when we get to logic)
# these are not the only types, but they are the 'primitives'

# float refers to a "floating point number". It means a number with a decimal point, so any real number. I like to imagine the name refers to the decimal point floating around (which I think it kind of does mean that)
# there are also integers, which are the same as integers in math. Integers cannot have decimal points

string_one = "1"

float_one = float(string_one) # turns "1" into 1 as a float aka decimal number type

int_one = int(string_one) # this makes an integer number

print('string to float', string_one, float_one)
print('string to int', string_one, int_one)

# string_half = "0.5"
# int_round1 = int(string_half) <--- this will crash the program!
# 
# if you try to convert a number with a decimal using int() the program will crash. This is the same as trying to convert a word to a number for example
# later we will learn ways to attempt this conversion without crashing if it doesnt work
# still, these errors can be difficult to detect before running the program, so they are an issue for python developers

# converting a float to an int however does work, it will just truncate the value removing any decimals (so basically it always rounds down)

float_value = 1.9

int_round2 = int(float_value)

print('float to int', float_value, int_round2)

# you can still pass number values to print and it will work fine

# if you add a number and a string the program will be angry:

print( string_one + int_one )

