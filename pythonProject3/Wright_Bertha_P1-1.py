### Program

''' Bertha Wright: Program 1-1
Date: 5-Sep-2022
Assignment: Week 02
Pseudocode: None Needed
'''

### Main Program
temp = (input("What is the the temperature? Put C or F at the end."))
if "C" in temp:
    non= temp.replace("C","")
    temp = float(non)
    Fahrenheit = (temp * (9/5)) + 32
    print(Fahrenheit, end="F")
elif "F" in temp:
    non= temp.replace("F","")
    temp = float(non)
    Celsius = (temp-32) * (5/9)
    print(Celsius, end="C")


