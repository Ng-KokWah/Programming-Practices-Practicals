"""
This is to create a list

Items in a list can be mutated aka can be modified or changed unlike tuples
"""
# Index starts from 0
friends = ["Kevin", "Karen", "Jim"]  # Can also store other types, e.g. "kate", 4, true

print(friends)  # Prints the entire list out
print(friends[0])  # Prints the element at the index of 0 aka first item on the list aka kevin
print(friends[-1])  # This index the list from behind so it becomes the last index element instead
print(friends[1:])  # This allows you to print out whatever that starts from index 1 onwards
print(friends[1:2])  # Gets elements in index 1 and 2, so karen and jim

friends[1] = "Mike"
print(friends[1])
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friend_list = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

print(friend_list)  # Original list
friend_list.append("Creed")  # Adds another item to the end of the list
print(friend_list)  # After appending

friend_list.insert(1, "Kelly")  # Adds an item to a specific index in the list and pushes the rest back
print(friend_list)

friend_list.remove("Kelly")  # This removes a specific item from the list
# Also known as a stack, First-In-Last-Out
friend_list.pop()  # This removes the last element in the list
print(friend_list)  # Before Extending

# NOTE DO NOT PUT IN ANYTHING THAT IS NOT IN THE LIST IT RESULTS IN ERROR
print("Index of Kevin: " + str(friend_list.index("Kevin")))  # Returns an index of where this item is found in the list

print("Number of times Jim appears in list: " + str(friend_list.count("Jim")))  # Count the number of times Jim appears in the list

friend_list.extend(lucky_numbers)  # This basically joins the two lists together
print(friend_list)  # After Extending list

friend_list.clear()  # Clears out the entire list
print(friend_list)

friends_list = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends_list.sort()  # Sorts the elements in the list in order
print(friends_list)

friends_list.reverse()  # Sorts the elements in the list in reverse order
print(friends_list)

friends2 = friends_list.copy()  # makes a copy of the friends_list
print(friends2)
