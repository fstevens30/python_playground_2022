#initial converter
"""
import math

#Initial savings per day
grainPerDay = 18.1437
litrePerDay = 4163.953
forestPerDay = 2.78709
animalPerDay = 1

#Introduction
print("Welcome to the Vegan Statistics Calculator!\n")
print("Enter how many days you have been vegan.\n")
print("Or how many days you plan to try out veganism.\n")

#Get the number of days
days = int(input("How many days: "))

#math
grainSave = math.floor(grainPerDay * days)
litreSave = math.floor(litrePerDay * days)
forestSave = math.floor(forestPerDay * days)
animalSave = math.floor(animalPerDay * days)

#Print results

print("\nYou have saved " + str(grainSave) + " kilograms of grain.")
print("You have saved " + str(litreSave) + " litres of water.")
print("You have saved " + str(forestSave) + " m2 of forest.")
print("You have saved " + str(animalSave) + " animals.")
"""
#this works well but i can make it look nicer and make the inputs easier

#setup

import math

#intro

print("Welcome to the Vegan Statistics Calculator!\n")
print("This tool will help you find out how much you can save over a period of time under a vegan lifestyle.\n")

#initial math, converting day month and year to days

numDays = int(input("How many days have you been vegan: \n"))
numMonths = int(input("How many months have you been vegan: \n"))
numYears = int(input("How many years have you been vegan: \n"))

totalDays = numDays + (numMonths * 30) + (numYears * 365)

#display total time vegan

print("You have been vegan for " + str(numYears) + " years, " + str(numMonths) + " months, and " + str(numDays) + " days.")
print("That is a total of " + str(totalDays) + " days.\n")

#assigning variables

grainPerDay = 18.1437
litrePerDay = 4163.953
forestPerDay = 2.78709
animalPerDay = 1

#math

grainSave = "{:.}".format(math.floor(grainPerDay * totalDays))
litreSave = "{:.}".format(math.floor(litrePerDay * totalDays))
forestSave = "{:.}".format(math.floor(forestPerDay * totalDays))
animalSave = "{:.}".format(math.floor(animalPerDay * totalDays))

#Print results

print("\nYou have saved " + str(grainSave) + " kilograms of grain.")
print("You have saved " + str(litreSave) + " litres of water.")
print("You have saved " + str(forestSave) + " m2 of forest.")
print("You have saved " + str(animalSave) + " animals.")




