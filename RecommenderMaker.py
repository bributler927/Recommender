import RecommenderEngine
from RecommenderEngine import recommendations, averages
import operator
def makerecs(name,items,ratings,size,top):
    notseen = []
    seen = []
    newdic = {}
    recommend = RecommenderEngine.recommendations(name, items, ratings, size)
    for title in items:
        for k,v in recommend:
            if title == k:
                newdic[title] = v
    for num in range(len(ratings[name])):
        if ratings[name][num] == 0:
            title = items[num]
            value = newdic[title]
            notseen.append((title, value))
        else:
            title = items[num]
            value = newdic[title]
            seen.append((title, value))
    seen = [item for item in sorted(seen, key = operator.itemgetter(1), reverse = True)]
    notseen = [item for item in sorted(notseen, key = operator.itemgetter(1), reverse = True)]
    topsim = seen[:(top)]
    #if student has seen it
    toprec = notseen[:(top)]
    #if student hasn't seen it
    return ((topsim, toprec))

#print(makerecs('student1367', ['127 Hours', 'The Godfather', '50 First Dates', 'A Beautiful Mind', 'A Nightmare on Elm Street', 'Alice in Wonderland', 'Anchorman: The Legend of Ron Burgundy', 'Austin Powers in Goldmember', 'Avatar', 'Black Swan'], {'student1367':[0, 3, -5, 0, 0, 1, 5, 1, 3, 0], 'student1046': [0, 0, 0, 3, 0, 0, 0, 0, 3, 5], 'student1206': [-5, 0, 1, 0, 3, 0, 5, 3, 3, 0], 'student1103': [-3, 3, -3, 5, 0, 0, 5, 3, 5, 5]}, 2, 3))
