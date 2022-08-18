from app.sense_distributor import *
from app.populate_db import *
import random


class Services:

    def __init__(self):
        self.repo = MysqlRepository()

    def instantiatedb(self, url):
        DBP = DB_Populator()
        data = DBP.getdata(url)
        DBP.populate_lemmas(data)
        DBP.populate_vectors(data)
        DBP.populate_sentences(data)
        DBP.populate_lexicon()
        return {'msg':'success'}

    def findsenses(self, target):
        vectors = self.repo.load_vectors()
        assert target in vectors.keys(), 'Target word is not in context.'
        sentences = self.repo.load_context_sent()
        lexicon = self.repo.load_lexicon()
        result = SenseDistributor(target, vectors, sentences, lexicon) #result.senses will be a list of senses objects
        return result

    def reset_db(self):
        RDB = DB_Populator()
        RDB.emptydb()





