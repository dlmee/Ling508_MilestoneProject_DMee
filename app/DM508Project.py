


if __name__ == '__main__':
    url = 'http://localhost:8000/Scrapes/GM_TPaC.html'
    texts = scrapePG(url)
    print(texts[:10])
    """
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
    print(type(tvec.targvectors[0]))"""


