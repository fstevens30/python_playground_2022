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
