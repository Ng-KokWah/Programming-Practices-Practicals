"""
    Special structure in python that allows us to store information
    in key value pairs, so that when you want to access this information,
    you can do so using the key
"""

# Must always include a comma after each key value pair
# It can also be numbers, e.g. 0: "January", etc
# NOTE KEYS MUST ALWAYS BE UNIQUE
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])

# Alternative way to get the value in a dictionary
print(monthConversions.get("Dec"))

# If you know that you or the user might be passing in an invalid key
# Can always set a default value to return in case it matches nothing in the dictionary
print(monthConversions.get("Luv", "Not a valid key"))
