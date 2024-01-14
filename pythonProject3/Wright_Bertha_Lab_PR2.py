### Program

''' Bertha Wright: Python Review Exercise Two
Date: 5-Sep-2022
Assignment: Week 02
Pseudocode: None Needed
'''

### Main Program

# A time traveler has suddenly appeared in your classroom!
# Prompt the user for the year that they are from
# and greet our strange visitor with a different message
# if he is from the distant past (before 1990),
# the present era (1990-2021) or from the future (beyond 2022).

year = int(input("Greetings! What is your year of origin? "))
if year <= 1990:
 print ("Wow, that's the past!")
elif year > 1990 and year <= 2022:
 print ("That's totally the present!")
else:
    print("Far out, that's the future!!")
