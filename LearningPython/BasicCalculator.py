num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

# Alternative
result = num1 + num2  # This however saves the user input as Strings
# Which means that this adds the string together or concat it
print(result)

# Solution, however this would not allow for numbers with decimal points
"""result = int(num1) + int(num2)
print(result)
"""

# Solution
result = float(num1) + float(num2)
print(result)
