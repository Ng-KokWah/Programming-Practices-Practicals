"""
    The inheritance example is in ChineseChef.py file

    Allows you to inherit functionality from another class in the new class
    e.g. ChineseChef inherits all the other make chicken, etc but is still able to create it's own special dish
"""
from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()
