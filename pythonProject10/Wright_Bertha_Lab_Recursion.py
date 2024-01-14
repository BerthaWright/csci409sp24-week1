### Program

''' Bertha Wright: Lab - Recursion
Date: 10-Oct-2022
Assignment: Week 07
Pseudocode: None Needed
'''

### Main Program


def number_raise(base_num, power_num):
    if power_num > 0:
        raises_num = base_num * number_raise(base_num, power_num-1)
    else:
        raises_num = 1
    return raises_num


num_base = int(input("What is the base number?"))
num_exponent = int(input("What is the exponent?"))
print(num_base, "raised to the power of", num_exponent, "is", number_raise(num_base, num_exponent), end=".")
