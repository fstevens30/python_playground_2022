# Python password generator
# Generate a random password of length 8 as a string
print("Python password generator");
import random; # Import the random module to generate a random number for the password
password = ""; # Create an empty string to store the password
for i in range(8): # Loop through 8 times to generate a password of length 8
    password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"); # Add a random character from the list of characters to the password   
print(password); # Print the password to the console



