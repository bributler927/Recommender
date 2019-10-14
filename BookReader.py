'''
BookReader.py'''
import os
'''def getdata():
    file = open("data/books.txt", 'r')
    bookrates = {}
    books = []
    for line in file:
        newline = line.split(',')
        student = newline[0]
        for book in newline[1::2]:
            if book not in books:
                books.append(book)
        
        if student not in bookrates:
            bookrates[student] = []
        bookrates[student] = newline[2::2]
    return (books,bookrates)'''

def getdata():
    bookfile = open("data/books.txt", 'r')
    books = []
    bookratings = {}
    for line in bookfile:
        info = line.split(",")
        student = info[0]
        if student not in bookratings:
            bookratings[student] = []
        for i in range(len(info[1:])):
            if i % 2 != 0:
                bookratings[student].append(int(info[i+1]))
            elif info[i+1] not in books:
                books.append(info[i+1])
    return(books, bookratings)
