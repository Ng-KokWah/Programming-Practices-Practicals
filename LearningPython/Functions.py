"""This defines a function, each line in this function
MUST BE INDENTED
else it is no longer a part of this particular function

You can also see the side of pycharm if it is part of the function
there should be an arrow to collapse the entire function
"""


def sayhi():
    print("Hello User!")


# It first goes to execute the top first before executing everything in the function
# before executing anything after it, as shown below
print("Top")
sayhi()
print("Bottom")


# Passing multiple parameters into a function
def say_hi(name, age):
    print("Hello, " + name + ", you are " + str(age))


say_hi("LOL", 35)
say_hi("Steve", 70)
