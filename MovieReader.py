'''
MovieReader.py'''
import os
def getdata():
    file = open("data/movies.txt", 'r')
    readfile = file.readline()
    movies = []
    ratings = {}
    ratingslist = {}
    for line in file:
        line = line.split(',')
        movie = line[1]
        student = line[0]
        score = line[2]
        if movie not in movies:
            movies.append(movie)
        if student not in ratings:
            ratings[student] = []
        ratings[student].append((movie,score))
        movies = sorted(movies)
    for rating in ratings.items():
        if rating[0] not in ratingslist:
            ratingslist[rating[0]] = []
        for i in range(len(movies)):
            ratingslist[rating[0]].append(0)
        for mov in rating[1]:
            for i in range(len(movies)):
                if movies[i] == mov[0]:
                    ratingslist[rating[0]][i] = int(mov[1])
    ratingslist['student1367'] = [0, 3, -5, 0, 0, 1, 5, 1, 3, 0, 5, 3, -3, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 3, 0, 1, 0, 0, -3, 1, 3, 1, 0, 0, 0, 0, 5, 0, 0, 1, 3, 0, 0, 0, 0, 0, 0, 5, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, -3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0]
    return((movies,ratingslist))
