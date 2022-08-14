from app.sense_distributor import *
from app.populate_db import *
import random


class Services:

    def __init__(self):
        self.repo = MysqlRepository()

    def instantiatedb(self):
        DBP = DB_Populator()
        url = 'http://host.docker.internal:8000/Scrapes/GM_TPaC.html'
        data = DBP.getdata(url)
        DBP.populate_lemmas(data)
        DBP.populate_vectors(data)
        DBP.populate_sentences(data)
        DBP.populate_lexicon()

    def findsenses(self, target):
        vectors = self.repo.load_vectors()
        assert target in vectors.keys(), 'Target word is not in context.'
        sentences = self.repo.load_context_sent()
        lexicon = self.repo.load_lexicon()
        result = SenseDistributor(target, vectors, sentences, lexicon) #result.senses will be a list of senses objects
        return result





