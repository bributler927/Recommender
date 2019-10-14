import operator
def averages(items, ratings):
    '''This function calculates the average ratings for items.
        In calculating averages, you should not count raters who give a v
        alue of 0 meaning "not rated". This means do not include them
        in the count for the denominator when calculating the averages.
        If no one rates an item, assign the value 0 as the rating.'''
    rateups = []
    itemplace = 0
    total = 0
    for item in items:
        divisi = []
        total = 0
        ratelist = []
        for rating in ratings.values():
            ratelist.append(rating)
        for rate in ratelist:
            if rate[itemplace] != 0:
                divisi.append(float(rate[itemplace]))
        else:
            pass
        for rate in divisi:
            total += rate
        if total == 0:
            rateups.append((items[itemplace], float(0)))
        else:
            avg = total / len(divisi)
            rateups.append((items[itemplace], float(avg)))
        itemplace += 1
    rateups = sorted(rateups)
    rateups = [item for item in sorted(rateups, key = operator.itemgetter(1), reverse = True)]
    return rateups

def similarities(name, ratings):
    '''This function calculates how similar the rater called name is to all
    other raters.
        A similarity measure can be calculated by finding the dot-product of
        two rating-lists.'''
    simildic = {}
    ind = 0
    comparelist = []
    longdic = {}
    #nametotal = 0
    for rate in ratings.items():
        if rate[0] == name:
            comparelist = rate[1]
            continue
        elif rate[0] not in simildic:
            simildic[rate[0]] = rate[1]
    for cuu in simildic.items():
        total = 0
        for num in range(0,(len(comparelist))):
            total += (comparelist[num] * cuu[1][num])
        longdic[cuu[0]] = total
    alphabetname = sorted(longdic.items())
    ratelist = [item for item in sorted(alphabetname, key = operator.itemgetter(1), reverse = True)]
    return ratelist

'''def recommendations(name, items, ratings, size):
    comparelist = similarities(name, ratings)
    comparelist = comparelist[:size]
    itemdic = {}
    enddic = {}
    recommdic = {}
    length = 0
    for person in comparelist:
        for people in person:
            if person[0] not in recommdic:
                recommdic[person[0]] = person[1]
    for score in range(0, len(items)):
        if items[score] not in itemdic:
            itemdic[items[score]] = 0
        for person in ratings.items():
            if person[0] == name:
                continue
            if person[0] not in recommdic:
                continue
            if person[1][score] == 0:
                itemdic[items[score]] = 
                continue
            else:
                itemdic[items[score]] += (recommdic[person[0]] * person[1][score])
    print(itemdic)
    for item in itemdic.items():
        if item[0] not in enddic:
                enddic[item[0]] = item[1]
        enddic[item[0]] /= float(size)
    enddic = [(item[0],item[1]) for item in sorted(enddic.items(), key = operator.itemgetter(1), reverse = True)]
    return enddic'''
def recommendations(name,items,ratings,size):
    comparelist = similarities(name, ratings)
    comparelist = comparelist[:size]
    itemdic = {}
    enddic = {}
    recommdic = {}
    for person in comparelist:
        for people in person:
            if person[0] not in recommdic:
                recommdic[person[0]] = person[1]
    for score in range(0, len(items)):
        length = 0
        if items[score] not in itemdic:
            itemdic[items[score]] = [0, 0]
        for person in ratings.items():
            if person[0] == name:
                continue
            if person[0] not in recommdic:
                continue
            if person[1][score] == 0:
                itemdic[items[score]] = [0, length + 1]
                continue
            else:
                itemdic[items[score]][0] += (recommdic[person[0]] * person[1][score])
    for item in itemdic.items():
        if item[0] not in enddic:
                enddic[item[0]] = item[1]
        enddic[item[0]][0] /= float(size - enddic[item[0]][1])
    enddic = [(item[0],float(item[1][0])) for item in sorted(enddic.items(), key = operator.itemgetter(1), reverse = True)]
    return enddic
