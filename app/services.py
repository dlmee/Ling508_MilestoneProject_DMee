from app.sense_distributor import *
from database.mysql_repository import *
import re

class Services:

    def __init__(self, target):
        self.repo = MysqlRepository()
        self.context = self.loadvectors()
        assert target in self.context.keys(), 'Target word is not in context.'
        self.result = self.splitsense(target, self.context)

    def loadvectors(self):
        sql = ('SELECT * '
               'FROM vectors '
               )
        self.repo.cursor.execute(sql)
        allvectors = list(self.repo.cursor) #NOTE, the answer from the cursor is given only ONCE!
        dictvectors = {}
        for vector in allvectors:
            separated = re.split(', ', vector[2])
            reconstituted = []
            for i, value in enumerate(separated):
                if i % 2 == 1:
                    if len(value) != 1:
                        value = 1
                    reconstituted.append((separated[i-1], int(value)))
            dictvectors[vector[0]] = reconstituted
        return dictvectors

    def splitsense(self, target, context):
        result = SenseDistributor(target, context)
        return result





if __name__ == '__main__':
    test = Services('animals')
    for line in test.result.senses:
        print(line.sense, line.surface, line.definition)

    searches = ['afternoon', 'beauty', 'animals', 'bed', 'diamonds', 'forget', 'inexorable', 'nails', 'radiant', 'sky', 'toys', 'young']
    results = []
    for word in searches:
        results.append(Services(word))
    for result in results:
        for line in result.result.senses:
            print(line.sense, line.surface, line.definition)




