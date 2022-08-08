from database.mysql_repository import *
from model.vectors import *
from model.lemmas import *
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re


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
def listtostring(list, max):
    longstring = ', '.join(list)
    return longstring[:max]

def dicttostring(dict, max):
    mergedlist = []
    for k, v in dict.items():
        mergedlist.append(k)
        mergedlist.append(str(v))
    longstring = ', '.join(mergedlist)
    return longstring[:max]

if __name__ == "__main__":

    url = 'http://localhost:8000/Scrapes/GM_TPaC.html'
    texts = scrapePG(url)

    #Need to create a set of all words in the texts.
    lexicon = Lexicon(texts)
    vectors = Vectorizer(texts)
    print(vectors.allvector['animals'])

    # lemma: lform, wforms (inflections)
    alllemmas = Lemma(lexicon.lex)
    lemset = set()
    for line in alllemmas.al:
        lemset.add((line[1], listtostring(line[2], 250)))
    lemlist = list(lemset)
    #repo = MysqlRepository()
    #repo.cursor.executemany("INSERT INTO lemma VALUES (%s, %s)", lemlist)

    # vectors: wform, lform, vecform
    vectlist = []
    for word in alllemmas.al:
        cleanvec = dicttostring(vectors.allvector[word[0]], 425)
        vectlist.append((word[0], word[1], cleanvec))

    #repo = MysqlRepository()
    #repo.cursor.executemany("INSERT INTO vectors VALUES (%s, %s, %s)", vectlist)



    #lexicon: id, wform, sense, subvect