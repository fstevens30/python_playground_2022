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


import math

days = years*365 or weeks*7
weeks = days/7
years = days/365


