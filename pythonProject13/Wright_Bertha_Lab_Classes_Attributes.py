### Program

''' Bertha Wright: Lab: Class Attributes and Methods
Date: 23-Oct-2022
Assignment: Week 09
Pseudocode: None Needed
'''


### Main Program

class Student:
    School = ""
    Mascot = ""

    def __init__(self, gpa, year):
        self.gpa = gpa
        self.year = str(year)


    def schoolmethod(self, School):
        School = Student.School


    def mascotmethod(self, Mascot):
        Mascot = Student.Mascot


    def __str__(self):
        return f"This student goes to {Student.School} and the mascot is {Student.Mascot}. Their gpa is {self.gpa}." \
               f"They are in their {self.year} year."

    def check_school(self, School):
        check = School == "CCU"
        if check is True:
            print("Go Teal!")
        else:
            print("You are missing out!")
