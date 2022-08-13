from app.sense_distributor import *
from database.mysql_repository import *
import re

class Services:

    def __init__(self):
        self.repo = MysqlRepository()


    def findsenses(self, target):
        print(target)
        vectors = self.repo.load_vectors()
        assert target in vectors.keys(), 'Target word is not in context.'
        sentences = self.repo.load_context_sent()
        lexicon = self.repo.load_lexicon()
        result = SenseDistributor(target, vectors, sentences, lexicon)
        return result



if __name__ == '__main__':
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
            print(line.sense, line.surface, line.definition, line.examples)




