# Colter Makowski
# UWYO COSC 1010
# Submission Date 11/10/24
# Lab 08
# Lab Section:15
# Sources, people worked with, help given to: Help given by Colton and Jedidiah
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
string = input("insert number here: ")
def check_if_int_or_float(string):
    try:
        if "." not in string:
            return int(string)
        elif string.count(".") == 1:
            return float(string)
        else:
            return False
    except ValueError:
        return False
number = check_if_int_or_float(string)
if number is not False:
    print("Converted value", number)
else:
    print("Invalid Input")


print("*" * 75)
# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
Output = []
def slope_intercept():
    while True:
        Output.clear()
        m = input("Slope here: ")
        m = check_if_int_or_float(m)
        if m is False:
            print("Please enter a valid slope value.")
            continue

        b = input("Intercept here: ")
        b = check_if_int_or_float(b)
        if b is False:
            print("Please enter a valid intercept value.")
            continue

        Low = input("Lower bound here: ")
        Low = check_if_int_or_float(Low)
        if Low is False:
            print("Please enter a valid lower bound value.")
            continue

        Up = input("Upper bound here: ")
        Up = check_if_int_or_float(Up)
        if Up is False or Low > Up:
            print("Please enter a valid upper bound: ")
            continue
        for number in range(int(Low), int(Up) +1):
            Y = m * number + b
            Output.append(Y)
        break
slope_intercept()
print(Output)



# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# (-b +or- square root(b^2-4ac))/2a
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
Answer = []
while True:
    Answer.clear()
    a = input("input x^2 term here: ")
    if a.lower() == "exit":
        break
    a = check_if_int_or_float(a)
    if a is False:
        print("Please enter a valid lower bound value.")
        continue
    if a == 0:
        print("Can't divide by 0")
        continue
    
    
    b = input("input x term here: ")
    if b.lower() == "exit":
        break
    b = check_if_int_or_float(b)
    if b is False:
        print("Please enter a valid lower bound value.")
        continue
    c = input("input constant term here: ")
    if c.lower() == "exit":
        break
    c = check_if_int_or_float(c)
    if c is False:
        print("Please enter a valid lower bound value.")
        continue
    z = b **2 - 4*a*c
    def root(z):
        if z < 0:
            return None
        else:
            return z ** 0.5
    if root(z) is None:
        print("values for root make imaginary number (i)")
        continue
    neg = (-b - root(z))/2*a
    pos = (-b + root(z))/2*a
    Answer.append(int(neg))
    Answer.append(int(pos))
    print(Answer)