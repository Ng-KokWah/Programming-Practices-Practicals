"""
    This imports the file of Student to use the student data type
"""
# From the student file i want to import the Student class
from Student import Student

# This is a student object
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 3.8, False)

print(student1.name)
print(student1.on_honor_roll())
