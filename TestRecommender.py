'''
@author: bributler
'''

import SmallDukeEatsReader
import RecommenderEngine
import MovieReader
import BookReader
import unittest

ratings = {"student1": [0, 2, 3], "student2": [1, 1, 1], "student3": [3, 2, 0]}
items = ["Cat", "Dog", "Bear"]

def driver():
    
    '''(items,ratings) = SmallDukeEatsReader.getdata()
    print("items = ",items)
    print("ratings = ", ratings)'''

    
    avg = RecommenderEngine.averages(items,ratings)
    print("average",avg)
    slist = RecommenderEngine.similarities("student1",ratings)
    print(slist)
    for key in ratings:
        slist = RecommenderEngine.similarities(key,ratings)
        print(key,slist)

    r3 = RecommenderEngine.recommendations("student1", items, ratings, 2)
    print(r3)
        
    print(MovieReader.getdata()[:5])
    print(BookReader.getdata()[:5])

class MyTest(unittest.TestCase):
    def test_averages(self):
        self.assertEqual(RecommenderEngine.averages(items, ratings), [('Bear', 2.0), ('Cat', 2.0), ('Dog', 1.6666666666666667)])
    def test_similarities(self):
        self.assertEqual(RecommenderEngine.similarities("student1", ratings), [('student2', 5), ('student3', 4)])
    def test_recommendations(self):
        self.assertEqual(RecommenderEngine.recommendations("student1", items, ratings, 2), [('Cat', 8.5), ('Dog', 6.5), ('Bear', 0.0)])
if __name__ == '__main__':
    #driver()
    unittest.main()
