
### Program

''' Bertha Wright: Program 1-3
Date: 26-Sep-2022
Assignment: Week 05
Pseudocode: None Needed
'''

### Main Program

import csv
with open("Transactions.csv") as transaction:
    actions = csv.reader(transaction)
    act_list = [row for row in actions]

beginning = float(input("What is the amount of money on hand? "))
total = beginning
i = 0
for item in act_list:
    if "P" in item:
        total -= float(act_list[i][1])
        i = i + 1
    elif "R" in item:
        total += float(act_list[i][1])
        i = i + 1

print("The final amount left is ", total, sep=" $")
if total >= beginning:
    print("Black")
if total <= beginning:
    print("Red")
