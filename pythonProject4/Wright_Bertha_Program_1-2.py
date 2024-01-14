### Program

''' Bertha Wright: Program 1-2
Date: 11-Sep-2022
Assignment: Week 03
Pseudocode: None Needed
'''

### Main Program


def large(num_list):
    print("1")
    big = num_list[0]
    for large in range(len(num_list)):
        if num_list[large] > big:
            big = num_list[large]
    print("The largest number is:", big)


def addition(num_list):
    add = 0
    for adding in num_list:
        add += adding
    print("The sum of the numbers is:", add)


def count(num_list):
    number = 0
    for num in num_list:
        number += 1
    print(number)


number_list = [112, 34, 58, 770, 37, 20, 90, 12, 67, 40]
menu = 0
while menu == 0:
    print("Menu")
    print("----------------------------------------")
    print("1. Find the largest number in the list: ")
    print("2. Calculate sum of numbers in the list: ")
    print("3. Count the numbers in the list: ")
    print("q. Quit menu")
    customer = input("What is your choice?" )

    if customer == "1":
        large(number_list)
    elif customer == "2":
        addition(number_list)
    elif customer == "3":
        count(number_list)
    elif customer == "q":
        menu = 1
        print("Have a nice day!")