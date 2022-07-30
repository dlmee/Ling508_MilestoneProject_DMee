from app.DM508Project import *
from database.mysql_repository import *

def listtostring(list):
    longstring = '_'.join(list)
    return longstring[:200]


url = 'http://localhost:8000/GM_TPaC.html'
texts = scrapePG(url)
vectors = Vectorizer(texts)
newword = Word('believe', texts)
print(len(newword.lex))
ALLWORDS = []
for i, word in enumerate(newword.lex[:100]):
    if len(word) > 3:
        instance = Word(word, texts)
        print(i, instance.lemma, instance.inflections)
        longstring = listtostring(instance.inflections)
        print(longstring)
        lemma = instance.lemma
        ALLWORDS.append((i, lemma, longstring))

repo = MysqlRepository()

repo.cursor.executemany("INSERT INTO lemma VALUES (%s, %s, %s)", ALLWORDS)
