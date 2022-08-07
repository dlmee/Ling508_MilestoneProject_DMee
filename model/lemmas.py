import re
from nltk.corpus import stopwords

class Lexicon:
    def __init__(self, corpus):
        sw = stopwords.words('english')
        self.lex = self.listlexicon(corpus, sw)

    def listlexicon(self, lexicon, sw):
        lexicon = [line.lower() for line in lexicon]
        lexset = set()
        for paragraph in lexicon:
            allwords = re.findall('\w+', paragraph)
            for words in allwords:
                if words not in sw:
                    lexset.add(words)
        lex = list(lexset)
        lex = sorted(lex)
        #self.wordflow = ' '.join([str(w) for w in self.lex])
        return lex


class Lemma:
    def __init__(self, lexicon):
        self.al = []
        for word in lexicon:
            lemma, inflections = self.findlemma(word, lexicon)
            self.al.append((word, lemma, inflections))

    def findlemma(self, word, lexicon):
        lemma = ''
        inflections = []
        poslemma = [word]
        for i in range(len(word)):
            if len(word)-i > 2:
                poslemma.append(word[0:-1-i])
        plemmas = {}
        poslemma.sort(key= lambda x:len(x))

        for pl in poslemma:
            lm = []
            for posword in lexicon:
                if re.match(pl, posword):
                    lm.append(posword)
                plemmas[pl] = lm
            if len(lm) > len(inflections)/5:
                lemma = pl
                inflections = plemmas[pl]
        return lemma, inflections