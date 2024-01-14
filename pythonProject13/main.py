### Program

''' Bertha Wright: Program 2-1
Date: 23-Oct-2022
Assignment: Week 09
Pseudocode: None Needed
'''
from Wright_Bertha_Lab_Classes_Attributes import Student

### Calling Class

students = int(input("How many students do you want to enter information for?"))
Student.School = input("Where do these students go?")
Student.Mascot = input("What is the mascot of the school?")
for student in range(students):
    gpa = float(input("What is the gpa of this student?"))
    year = input("What year is this student?")
    stud = Student(gpa, year)
    stud.check_school(Student.School)
    print(f"Tell them to make sure their gpa, which is {stud.gpa}, is higher than a 2.0!")
    print(stud)


