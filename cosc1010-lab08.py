# Colter Makowski
# UWYO COSC 1010
# Submission Date 11/10/24
# Lab 08
# Lab Section:15
# Sources, people worked with, help given to:
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
list = []
def slope_intercept():
    while True:
        m = input("slope Here: ")
        if check_if_int_or_float(m):
            m = check_if_int_or_float(m)
        elif 'exit' in m.lower():
            break
        else:
            print ("Please enter correct value")
            continue
        B
        if check_if_int_or_float(B):
            B = check_if_int_or_float(B)
        elif 'exit' in B.lower

            Low = check_if_int_or_float(input())
        Up = check_if_int_or_float(input())
        if Low > Up:
            print ("Please enter correct value")
            continue
        For i in range(low, up +1):
            Y = m*i+ b
            list.append(Y)
slope_intercept()
print(list)



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
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
