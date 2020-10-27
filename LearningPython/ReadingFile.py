# Can use relative, absolute or just the filename (provided it is in the same directory)
# You can specify what mode you want to read the file in after the filename, e.g. "t.txt", "r" <Means read file only>
# Modes: r -> read (read file only), w -> write (can modify file),
# a -> append (append info to end of the file, but cannot modify existing info in the file)
# r+ -> read and write (can modify and read file)

employee_file = open("employees.txt", "r")

if employee_file.readable():
    # This reads one line of the file only
    # print(employee_file.readline())

    # This stores all the lines in the file as an array
    for employee in employee_file.readlines():
        print(employee)

# NOTE ALWAYS ENSURE THAT YOU CLOSE THE FILE AT SOME POINT
employee_file.close()
