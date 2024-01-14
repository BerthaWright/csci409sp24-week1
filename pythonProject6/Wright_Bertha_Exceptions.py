### Program

''' Bertha Wright: Exceptions
Date: 18-Sep-2022
Assignment: Week 04
Pseudocode: None Needed
'''

### Main Program

try:
    masks = int(input("Please enter the number of masks available:"))
except ValueError:
    print("That is not a valid number. Exiting now.")
    exit()


for want in range(masks):
    try:
        want = int(input("Please enter the number of masks you want."))
        masks -= want
        if masks <= 0 or masks == 0:
            print("Out of masks")
            break
        elif want <= 0:
            masks += want
            raise ValueError
        else:
            print(masks)
    except ValueError:
        print("Invalid entry. Please try again")
        continue
    finally:
        if masks <= 0 or masks == 0:
            print("Exiting program.")
            exit()
