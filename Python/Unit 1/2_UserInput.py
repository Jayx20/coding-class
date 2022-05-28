# user input

print("please enter something: ")
user_input = input()

# prompt the user

user_input = input("Please enter a funny number: ")

print("you inputted: ", user_input, sep='')

# calculator

num1 = input("Please enter the first number: ")
num2 = input("Please enter the number you'd like to multiply by: ")

print("The answer to this math problem,", num1, 'times', num2, 'is', num1+num2)

# this doesn't work because input always creates a string, which is a data type that means a list of characters. input() does not give us number values. 1 and "1" are different!
# to turn a string into a number, you can use float()

string_one = "1"

number_one = float(string_one) # turns "1" into 1 as a float aka decimal number type

print(float(num1) + float(num2)) # this works correctly because both were converted to numbers before the addition takes place
# also note the result of a float + float operation is still a float, but print() can display a float, not just a string
# note as well that calling one function inside of another function is perfectly valid. As you might guess because of the parentheses,
# the inner functions are executed first (so both numbers are converted to float before print is called)
