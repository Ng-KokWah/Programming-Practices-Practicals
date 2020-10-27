"""
    Appending text to the end of a file
    Files does not necessary need to be txt can also be html files, etc
"""
employee_file = open("employees.txt", "a")

# This adds this to a file on a newline
employee_file.write("\nToby - Human Resources")

employee_file.close()

"""
    Overwrite/Create a new file
    If you specify an existing file it would be overwritten but if you specify a file that does not exists
    while using the mode of write (w) then it would create a new file
"""

# This Overwrites the existing file
employee_file = open("employees.txt", "w")

if employee_file.writable():
    employee_file.write("\nKelly - Customer Service")

employee_file.close()

# This Creates a new file
employee_file = open("new_employees.txt", "w")

if employee_file.writable():
    employee_file.write("\nKelly - Customer Service")

employee_file.close()
