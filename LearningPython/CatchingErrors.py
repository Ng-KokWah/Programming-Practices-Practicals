try:
    # this would throw a ZeroDivisionError
    # value = 10/0

    # It is good practice to usually specify the error so that debugging is easier
    # If you just put except without any specific error any error that got it would just catch every single error
    # This usually would not cause an error but if the user enter anything other than a number, it would throw an error
    number = int(input("Enter a number: "))
    print(number)
# This prints out the specific error type
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input!")
