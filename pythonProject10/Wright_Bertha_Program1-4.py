### Program

''' Bertha Wright: Program 1-4
Date: 10-Oct-2022
Assignment: Week 07
Pseudocode: None Needed
'''


### Main Program


def counter(user):
    if user == "":
        char_count = 0
    else:
        char_count = 1 + counter(user[1:])
    return char_count


string = str(input("Please enter a string: "))
print("Your string has", counter(string), "characters.")
