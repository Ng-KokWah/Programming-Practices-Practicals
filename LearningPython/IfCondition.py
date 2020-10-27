is_male = True
is_tall = True

# Similar to functions, for if statements
# Everything after it that is indented will be executed
# can use the keyword or to check if either or both of the condition is met
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

# Can also use the keyword and to check that both conditions are met
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not male or not tall or both")


# Using else if to create a separate condition
# Can use keyword not to negate whatever is enclosed in brackets after it
# not flips whatever in it, so if its true, it would return false, etc
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not male and not tall")
