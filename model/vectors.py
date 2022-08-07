import re
from nltk.corpus import stopwords
from collections import Counter

class Vectorizer:
    def __init__(self, corpus):
        self.corpus = corpus
        self.ESW = stopwords.words('english')
        self.tokenize()
        self.dictasvector()

    def tokenize(self):
        self.refine = [line.lower() for line in self.corpus]
        self.refine = [re.findall('\w+', line) for line in self.refine]
        self.nrefine = self.stopwords(self.refine)

    def stopwords(self, listoftokens):
        newlist = []
        for line in listoftokens:
            newlist.append([token for token in line if token not in self.ESW])
        return list(newlist)

    def merge_nest_dict(self, dictword1, dictword2):
        dict1 = Counter(dictword1)
        dict2 = Counter(dictword2)
        dict3 = dict1 + dict2

        return (dict3)

    def dictasvector(self):
        self.allvector = {}
        tempvector = {}
        for line in self.nrefine:
            for word in line:
                if word in self.allvector:
                    nest = {}
                    for w2 in line:
                        if w2 != word:
                            nest[w2] = 1
                    tempvector[word] = nest
                    self.allvector[word] = self.merge_nest_dict(self.allvector[word], tempvector[word])
                else:
                    nest = {}
                    for w2 in line:
                        if w2 != word:
                            nest[w2] = 1
                    self.allvector[word] = nest


class Vector:
    def __init__(self, lemma, inflections, vectors):
        self.lemma = lemma
        self.inflections = inflections
        self.sourcevectors = vectors
        self.targvectors = []
        self.findtargets()

    def findtargets(self):

        for word in self.inflections:
            self.targvectors.append((word, self.sourcevectors[word]))