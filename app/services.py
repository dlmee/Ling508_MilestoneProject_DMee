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

    def random_sense(self):
        #lemmas = self.repo.load_lemmas()
        #index = random.randint(1, len(lemmas))
        #targets = lemmas[index][2]
        #target = targets[random.randint(0, len(targets))]
        vectors = self.repo.load_vectors()
        sentences = self.repo.load_context_sent()
        lexicon = self.repo.load_lexicon()
        result = SenseDistributor('animals', vectors, sentences, lexicon)
        return result



'''if __name__ == '__main__':
    services = Services() #Need to make it so the services layers can implement multiple use cases.
    test = services.findsenses('animals')
    for line in test.senses:
        print(line.sense, line.definition, line.examples)
    #For use case 1 i want services.senses
    #For use case 2 i want services.usecase2
    #Separate the class by methods for various use cases. See diagram in project overview.

    searches = ['afternoon', 'beauty', 'animals', 'bed', 'diamonds', 'forget', 'inexorable', 'nails', 'radiant', 'sky', 'young']
    results = []
    listservices = Services()
    for word in searches:
        results.append(listservices.findsenses(word))
    for result in results:
        for line in result.senses:
            print(line.sense, line.surface, line.definition, line.examples)'''




