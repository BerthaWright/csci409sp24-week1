### Program

''' Bertha Wright: Python Review 2 Exercise 2
Date: 11-Sep-2022
Assignment: Week 03
Pseudocode: None Needed
'''

### Main Program

def avg(num):
    addition = 0
    for user in num:
        addition += user
    print("The average is:", addition / len(num))


numberlist = []
num = 0
print('Please enter numbers. When you are done enter a "q" to get the average.')
while num == 0:
    user = (input("Please enter a number here:"))
    if user == "q":
        num = 1
        complete = avg(numberlist)
        print(complete)
    else:
        numberlist.append(float(user))
