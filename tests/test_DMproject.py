from app.services import *
from model.senses import *

#Week 5 Tests

def test_usecase1():
    test = Services('animals')
    for line in test.result.senses:
        assert (type(line)) == Senses
        assert line.surface == 'animals'
        assert type(line.sense) == int
        assert type(line.definition) == list

#Week 4 Tests
'''
def test_SQLdatabase():
    repo = MysqlRepository()
    sql = ('SELECT COUNT(*) '
           'FROM lemma')
    repo.cursor.execute(sql)
    answer = (list(repo.cursor))
    assert answer[0][0] == 92
'''

#Week 3 Tests
'''
def test_Word():
    word = 'believe'
    url = 'http://localhost:8000/GM_TPaC.html'
    texts = scrapePG(url)
    lm = Word('believe', texts)
    assert type(lm.lemma) == str
    assert type(lm.inflections) == list
    assert len(lm.inflections) > 0

def test_Vectorizer():
    url = 'http://localhost:8000/GM_TPaC.html'
    texts = scrapePG(url)
    vectors = Vectorizer(texts)
    assert type(vectors.allvector) == dict
    assert type(vectors.allvector['crown']['king']) == int

def test_Vector():
    url = 'http://localhost:8000/GM_TPaC.html'
    texts = scrapePG(url)
    vectors = Vectorizer(texts)
    word = Word('believe', texts)
    tvec = Vector(word.lemma, word.inflections, vectors.allvector)
    assert type(tvec.targvectors) == list
    assert type(tvec.targvectors[0]) == tuple
    assert type(tvec.targvectors[0][0]) == str
    assert tvec.targvectors[0][1]['knew'] == 1
'''

