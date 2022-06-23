# I aim to make a simple currency converter using an input of USD
usd = input("Enter USD amount ")

# Get user to confirm

import click

if click.confirm("You entered, " + str(usd) + " is this correct?", default=True):
    print("Select the currency you want to convert to")

# Currencies

print(
    str(
        """CAD - C
AUD - A
NZD - N
GBP - G
CNY - Y
EUR - E"""
    )
)
currency = input("Enter the desired currency (e.g for CAD, type C)")

# Math for conversions using match-case statement


def convert(currency):
    match currency:
        case "C", "c":
            return usd * 1.2974511
        case ":
            return usd * 1.4511509
        case N:
            return usd * 1.5977626
        case G:
            return usd * 0.81711593
        case Y:
            return usd * 6.7117017
        case E:
            return usd * 0.94678294
        case _:
            return "Error: Incorrect input"


print(convert)
