"""
    Made up language conditions
    all vowels: a, e, i, o, u
    are converted into g
    e.g. dog -> dgg, cat -> cgt
"""


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "G"
            else:
                translation += "g"
        else:
            translation += letter
    return translation


print(translate(input("Enter a phrase: ")))
