from Ling508MP_DMee.app import sensedist
from app.sensedist import *

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