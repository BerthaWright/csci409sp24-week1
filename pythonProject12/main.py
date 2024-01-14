### Program

''' Bertha Wright: Lab: Classes and Objects
Date: 23-Oct-2022
Assignment: Week 09
Pseudocode: None Needed
'''

### Main Program

class Address:
        def __init__(self):
            self.house_number = 0
            self.street_name = ""
            self.city = ""
            self.state = ""
            self.postalcode = 0

        def address_list(self):
            ad = [self.house_number, self.street_name, self.city, self.state, self.postalcode]
            print(ad)


address1 = Address()
address1.house_number = 4059
address1.street_name = "Mount Lee Drive"
address1.city = "Los Angeles"
address1.state = "California"
address1.postalcode = 90068
address1.address_list()

address2 = Address()
address2.house_number = 90
address2.street_name = "Bedford St"
address2.city = "New York City"
address2.state = "New York"
address2.postalcode = 10014
address2.address_list()
