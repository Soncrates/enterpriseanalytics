import collections, re

class wordbag :
    @staticmethod
    def action(*text_list) :
        bagsofwords = [ collections.Counter(re.findall(r'\w+', txt)) for txt in texts]
        sumbags = sum(bagsofwords, collections.Counter())
        return bagsofwords, sumbags

if __name__ == "__main__" :
   texts = ['John likes to watch movies. Mary likes too.', 'John also likes to watch football games.']
   bagsofwords, sumbags = wordbag.action(*texts)
   print bagsofwords[0]
   print bagsofwords[1]
   print sumbags
'''
Counter({'likes': 2, 'watch': 1, 'Mary': 1, 'movies': 1, 'John': 1, 'to': 1, 'too': 1})
Counter({'watch': 1, 'games': 1, 'to': 1, 'likes': 1, 'also': 1, 'John': 1, 'football': 1})
Counter({'likes': 3, 'watch': 2, 'John': 2, 'to': 2, 'games': 1, 'football': 1, 'Mary': 1, 'movies': 1, 'also': 1, 'too': 1})
'''
