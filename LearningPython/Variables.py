from math import *  # Imports everything from Math Module

"""Variable Types"""
character_name = "John"     # String
character_age = 35      # Integer
is_male = True      # Boolean

print("Hello, " + character_name)

"""Working with strings"""
phrase = "Test"

print(phrase.upper())  # Convert to uppercase
print(phrase.lower())  # Convert to lowercase
print(phrase.isupper())     # Checks if the phrase is in uppercase
print(phrase.islower())     # Checks if the phrase is in lowercase
print(len(phrase))  # Prints the length of the string
print(phrase[0])    # Get the first character in the string
# DO NOT PUT ANY CHARACTER THAT IS NOT FOUND IN THE STRING
print(phrase.index("T"))    # Finds the index of a specified character
print(phrase.replace("Te", "LOL"))  # Replace letters in the string

"Working With Numbers"
print(3 + 4.5)  # Any operations can also work
print(10 % 3)   # Returns 1 cause its the remainder of 10 divide by 3 aka 10 mod 3

my_num = -5
print(abs(my_num))  # Prints the absolute number of the variable and since it is -5 it will print 5

# Functions without using the Math module
print(pow(3, 2))    # 3 to the power of 2 which is 9
print(max(4, 6))    # Returns the larger number of the two
print(min(4, 6))    # Returns the smaller number of the two
print(round(3.2))  # Round the number, as per usual 3.2 returns 3, while 3.7 returns 4

# Functions in the Math module
print(floor(3.7))  # Which rounds down the number no matter if its 3.1 or 3.7
print(ceil(3.7))    # Always rounds up the number no matter if its 3.1 or 3.7
print(sqrt(36))     # Returns the square root of the number
