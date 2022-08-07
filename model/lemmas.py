

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