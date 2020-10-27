# As with other programming language this allows you to control the number of times a certain code is repeated

# letter can be substituted with any other word you want
for letter in "Hello World":
    print(letter)

# looping through a list
friends = ["Jim", "Karen", "Kevin"]
# friend can be substituted with any other word you want
for friend in friends:
    print(friend)

# This can also be done using a range
# This prints everything since the length of the list is 3 while the index is 0, 1, 2 only
for f in range(len(friends)):
    print(friends[f])

# This prints up to 9 but not including 10
for index in range(10):
    print(index)

# This prints from 3 to 9 but not including 10
for i in range(3, 10):
    print(index)
