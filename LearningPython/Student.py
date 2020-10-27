"""
    This is just to be used in another python file
    MAIN PYTHON FILE: ClassesObjects.py
"""


# Defines a student data type
class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        # This means that the actual object's name is equal to what the app passes in when creating the object
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    # Functions
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
