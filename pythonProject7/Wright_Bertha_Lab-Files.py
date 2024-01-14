### Program

''' Bertha Wright: Lab-Files
Date: 26-Sep-2022
Assignment: Week 05
Pseudocode: None Needed
'''

### Main Program

lab = open("file_lab.txt")
lines = lab.read()
count = 1
for words in lines:
    if words == " " or words == "\n":
        count += 1
print("There are", count, "words in the text file.")
