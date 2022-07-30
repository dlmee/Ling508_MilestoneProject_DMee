from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
from collections import Counter

def scrapePG(url):
    try:
        source = urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
    else:
        bs = BeautifulSoup(source.read(), 'html.parser')
        paragraphs = []
        for paragraph in bs.div.find_all('p', class_=False):
            if len(paragraph.get_text()) > 4:
                paragraphs.append(paragraph.get_text())
        paragraphs = paragraphs[0:-23]
        sentences = []
        for i, paragraph in enumerate(paragraphs):
            paragraph = re.sub('[\n\"\-\',\[\d\]]', ' ', paragraph)
            sents = re.split('[\.\!\?]', paragraph)
            for s in sents:
                sentences.append(s)
        return sentences

#Input, a word. Output: a lemma
class Word:
    def __init__(self, word, lexicon):
        self.surface = word
        self.listlexicon(lexicon)
        self.findlemma(word)
        #self.lemma = word
    def listlexicon(self, lexicon):
        lexicon = [line.lower() for line in lexicon]
        lexset = set()
        for paragraph in lexicon:
            allwords = re.findall('\w+', paragraph)
            for words in allwords:
                lexset.add(words)
        self.lex = list(lexset)
        self.lex = sorted(self.lex)
        #self.wordflow = ' '.join([str(w) for w in self.lex])

    def findlemma(self, word):
        lemmatch = []
        poslemma = [word]
        for i in range(len(word)):
            if len(word)-i > 2:
                poslemma.append(word[0:-1-i])
        #print(poslemma)
        plemmas = {}

        for pl in poslemma:
            lm = []
            for posword in self.lex:
                if re.match(pl, posword):
                    lm.append(posword)
                plemmas[pl] = lm
            if len(pl) == 4:
                self.lemma = pl
                self.inflections = plemmas[pl]
        return

#Initially I had a Lemma class, but I'm not sure if I need that, because I'm finding that using the inflections is how I find the lemma.

#Input, list of inflections. Output: list of target vectors
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

#Input, list of tokenized sentences. Output: List of dictionary of dictionaries
#Used code from my internship to run. The beauty of classes emerges! A microservice applied in different contexts.

class Vectorizer:
    def __init__(self, corpus):
        self.corpus = corpus
        self.BISW = stopwords.words('english')
        self.tokenize()
        self.dictasvector()

    def tokenize(self):
        self.refine = [line.lower() for line in self.corpus]
        self.refine = [re.findall('\w+', line) for line in self.refine]
        self.nrefine = self.stopwords(self.refine)

    def stopwords(self, listoftokens):
        newlist = []
        for line in listoftokens:
            newlist.append([token for token in line if token not in self.BISW])
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




if __name__ == '__main__':
    url = 'http://localhost:8000/GM_TPaC.html'
    texts = scrapePG(url)
    vectors = Vectorizer(texts)
    newword = Word('believe', texts)
    print(len(newword.lex))
    ALLWORDS = []
    for word in newword.lex[100]:
        ALLWORDS.append(Word(word, texts))
    print(vectors.allvector['crown']['king'])
    print(type(vectors.allvector))
    tvec = Vector(newword.lemma, newword.inflections, vectors.allvector)
    print(tvec.targvectors[0])
    print(type(tvec.targvectors[0]))


