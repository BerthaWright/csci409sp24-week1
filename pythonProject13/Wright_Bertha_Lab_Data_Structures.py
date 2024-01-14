### Program

''' Bertha Wright: Lab: Data Structures
Date: 28-Nov-2022
Assignment: Week 13
Pseudocode: None Needed
'''


### Main Program


class Library_Stack:

    def __init__(self):
        self.Library = []

    def Stack_Push(self, book):
        self.Library.append(book)

    def Stack_Pop(self,):
        return self.Library.pop()

book = Library_Stack()
book.Stack_Push("Lord of the rings")
book.Stack_Push("Harry Potter and the Chamber of Secrets")
book.Stack_Push("Percy Jackson and the Lightning Thief")
book.Stack_Push("The Hunger Games")
book.Stack_Push("Fablehaven")
for items in book.Library:
    print(book.Stack_Pop())

class Line_Queue:

    def __init__(self):
        self.Line = []

    def Line_Insert(self, person):
        self.Line.insert(0, person)

    def Line_Pop(self):
        return self.Line.pop()



Person = Line_Queue()
Person.Line_Insert("Ginny")
Person.Line_Insert("Annabeth")
Person.Line_Insert("Ron")
Person.Line_Insert("Peeta")
Person.Line_Insert("Seth")
for people in Person.Line:
    print(Person.Line_Pop())