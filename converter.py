# I aim to make a simple currency converter using an input of USD
usd = input("Enter USD amount ")

# Get user to confirm

from unittest import result
import click

if click.confirm("You entered, " + str(usd) + " is this correct?", default=True):
    print("Select the currency you want to convert to")

# Currencies

print(
    str(
        """CAD - 1
AUD - 2
NZD - 3
GBP - 4
CNY - 5
EUR - 6"""
    )
)
currency = input("Enter the desired currency (e.g for CAD, type )")

# If statement for conversion

if currency == 1:
    print(str(usd * 1.2974511))
     currency == 2:
        print(str(usd * 1.4511509))


# Math for conversions using match-case statement

"""
def convert(currency):
    match currency:
        case 1:
            return usd * 1.2974511
        case 2:
            return usd * 1.4511509
        case 3:
            return usd * 1.5977626
        case 4:
            return usd * 0.81711593
        case 5:
            return usd * 6.7117017
        case 6:
            return usd * 0.94678294
        case _:
            return print("Error: Incorrect input")


print(convert(currency))
"""
