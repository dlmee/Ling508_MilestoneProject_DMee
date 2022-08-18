from app import collectdata
from app.services import *
import app.collectdata
from model.lemmas import *

def test_Word():
    word = 'believe'
    url = 'http://localhost:8000/GM_TPaC.html'
    texts = collectdata.CollectData.scrape(url)
    lm = Lemma('believe', texts)
    assert type(lm.lemma) == str
    assert type(lm.inflections) == list
    assert len(lm.inflections) > 0

def test_Vectorizer():
    url = 'http://localhost:8000/GM_TPaC.html'
    texts = collectdata.CollectData.scrape(url)
    vectors = Vectorizer(texts)
    assert type(vectors.allvector) == dict
    assert type(vectors.allvector['crown']['king']) == int

def test_Vector():
    url = 'http://localhost:8000/GM_TPaC.html'
    texts = collectdata.CollectData.scrape(url)
    vectors = Vectorizer(texts)
    word = Lemma('believe', texts)
    tvec = Vector(word.lemma, word.inflections, vectors.allvector)
    assert type(tvec.targvectors) == list
    assert type(tvec.targvectors[0]) == tuple
    assert type(tvec.targvectors[0][0]) == str
    assert tvec.targvectors[0][1]['knew'] == 1