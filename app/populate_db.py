from app.collectdata import *
from database.mysql_repository import *
from model.vectors import *
from model.lemmas import *


class DB_Populator:
    def __init__(self):
        self.repo = MysqlRepository()

    def getdata(self, source):
        datacollection = CollectData()
        self.data = datacollection.scrapePaC(source)
        return self.data

    def populate_lemmas(self, texts):
        # lemma: id, lform, wforms
        lexicon = Lexicon(texts)
        all_lemmas = Lemma(lexicon.lex)
        lemset = set()
        for line in all_lemmas.al:
            lemset.add((line[1], self.listtostring(line[2], 250)))
        lemlist = list(lemset)
        self.repo.cursor.executemany("INSERT INTO lemma VALUES (0, %s, %s)", lemlist)
        return

    def populate_vectors(self, texts):
        # vectors: wform, lform, vecform
        lexicon = Lexicon(texts)
        vectors = Vectorizer(texts)
        all_lemmas = Lemma(lexicon.lex)

        vectlist = []
        for word in all_lemmas.al:
            cleanvec = self.dicttostring(vectors.allvector[word[0]], 425)
            vectlist.append((word[0], word[1], cleanvec))

        self.repo.cursor.executemany("INSERT INTO vectors VALUES (%s, %s, %s)", vectlist)
        return

    def populate_lexicon(self):
        # lexicon: id, wform, indexed sentences
        # Load the lexicon last, that way we can use the context_sentences part of the db to populate the indexed sentences.
        dbwords = self.repo.load_lemmas()
        dbsents = self.repo.load_context_sent()
        lexdict = {}
        for triad in dbwords:
            for word in triad[2]:
                if word not in lexdict.keys():
                    indices = []
                    for sentence in dbsents:
                        if word in sentence[3]:
                            indices.append(sentence[0])
                    lexdict[word] = indices
        lexemes = []
        for k, v in lexdict.items():
            if len(v) > 0:
                lexemes.append((k, str(v)[:500]))
        self.repo.cursor.executemany("INSERT INTO lexicon VALUES (0, %s, %s)", lexemes)

    def populate_sensicon(self, senses):
        pass

    def populate_sentences(self, texts):
        # contextsentences: chapter, sentence, vecfriendly
        vectors = Vectorizer(texts)
        fillcheck = []
        for sentence in vectors.contextsentences:
            if len(sentence[2]) > 2:
                fillcheck.append(sentence)
        self.repo.cursor.executemany("INSERT INTO context_sentences VALUES (0, %s, %s, %s)", fillcheck)

    def listtostring(self, list, max):
        longstring = ', '.join(list)
        return longstring[:max]

    def dicttostring(self, dict, max):
        mergedlist = []
        for k, v in dict.items():
            mergedlist.append(k)
            mergedlist.append(str(v))
        longstring = ', '.join(mergedlist)
        return longstring[:max]

'''if __name__ == "__main__":
    DBP = DB_Populator()
    url = 'http://localhost:8000/Scrapes/GM_TPaC.html'
    data = DBP.getdata(url)
    DBP.populate_lemmas(data)
    DBP.populate_vectors(data)
    DBP.populate_sentences(data)
    DBP.populate_lexicon()'''
