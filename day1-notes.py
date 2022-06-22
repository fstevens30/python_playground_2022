# Welcome to Python playground

# Comments on single lines are made with #

# We can print to console using print e.g

print("Hello World!")

# Printing two string together

print("Hello " + "Flynn")

# Creating variables

todays_date = 22
todays_day = "Wednesday"

# Arithmetic in python

multiply = 4 * 4
divide = 4 / 2
add = 4 + 4
subtract = 4 - 2
remainder = 4 % 3

print(multiply)
print(remainder)

# Updating Variables
# example using annual rainfall
january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
annual_rainfall += september_rainfall

october_rainfall = 7.20
annual_rainfall += october_rainfall

november_rainfall = 5.06
annual_rainfall += november_rainfall

december_rainfall = 4.06
annual_rainfall += december_rainfall

print(annual_rainfall)

# Numbers

# Integers are numbers with no decimal point E.G

int1 = 1
int2 = 2
int3 = -3

print(int1, ",", int2, ",", int3)

# Float is a number with a decimal point
# You can also use "e" when declaring to indicate the power of 10

float1 = 1.0
float2 = 10.0
float3 = -5.5

# Using "e"

float4 = 1.5e2

print(float1)
print(float2)
print(float3)
print(float4)

# Grocery list activity
cucumbers = 3
price_per_cucumber = 3.25

total_cost = cucumbers * price_per_cucumber

print(total_cost)  # total_cost is a float

# Division

# THE FOLLOWING ONLY APPLIES TO PYTHON 2
# When dividing two integers they become rounded down instead of converting to float
# E.G

div1 = 7 / 2
print(div1)  # Prints 3 instead of 3.5 in python 2

# To overcome this we can make a value or two floats e.g
div2 = 7.0 / 2
print(div2)

# Cucumbers division with python 2 activity

cucumbers = 100
num_people = 6
whole_cucumbers_per_person = cucumbers / num_people
print(whole_cucumbers_per_person)  # In python 2 this prints 16

float_cucumbers_per_person = float(cucumbers) / num_people
print(float_cucumbers_per_person)

# Multi-line strings

# Can be assigned to a variable and work as a multi line string otherwise are multi line comments
# E.g
""" This 
is a multi-line
comment
"""

haiku = """The old pond,
A frog jumps in:
Plop!
"""
print(haiku)

# Booleans
# Simple true or false e.g

isTrue = True
isFalse = False

# Code Academy example

# Hi! I'm Maria and I live in script.py.
# I'm an expert Python coder.
# I'm 21 years old and I plan to program cool stuff forever.
age_is_12 = False
name_is_maria = True

# Variable conversions to different datatypes
# E.g converting to string using str() method

float_1 = 0.25
float_2 = 40.0
product = float_1 * float_2
big_string = "The product was " + str(product)
print(big_string)

# Final Code Academy challenge

skill_completed = "Python Syntax"
exercises_completed = 13
# The amount of points for each exercise may change, because points don't exist yet
points_per_exercise = 5
point_total = 100
point_total += exercises_completed * points_per_exercise
print("I got " + str(point_total) + " points!")
