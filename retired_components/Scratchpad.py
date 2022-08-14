#This is code that I am no longer using, but want to hold onto just in case. To be deleted at a future date.

# DROP DATABASE IF EXISTS mcdonald;

'''
from sqldatabase.mysql_repository import *

repo = MysqlRepository()


sql = ('SELECT * '
       'FROM lemma '
       )
repo.cursor.execute(sql)
print(list(repo.cursor))

sql = ('SELECT COUNT(*) '
       'FROM lemma')

repo.cursor.execute(sql)
answer = (list(repo.cursor))
print(answer[0][0])

sql = ('DELETE FROM lexicon '
       'WHERE wordform = "bazinga" '
       )
repo.cursor.execute(sql)
print(list(repo.cursor))

for word in ['one', 'two', 'three', 'four']:
    sql = ('INSERT INTO lexicon '
           '(wordform, pos) '
           'VALUES '
           '("hello", "noun")'
           )
    repo.cursor.execute(sql)

sql = ('SELECT wordform, pos '
       'FROM lexicon '
       )
repo.cursor.execute(sql)
print(list(repo.cursor))

sql = ('INSERT INTO lemma '
       '(lform, sforms) '
       'VALUES '
       '("beli", "believe, belief, believed, believes, believing"), '
       '("see", "sees, seem, saw") '
       )
repo.cursor.execute(sql)

sql = ('SELECT id, lform, sforms '
       'FROM lemma '
       )
repo.cursor.execute(sql)
print(list(repo.cursor))

sql = ('DELETE FROM lemma '
       'WHERE id < 100'
       )
repo.cursor.execute(sql)

sql = ('SELECT id, lform, sforms '
       'FROM lemma '
       )
repo.cursor.execute(sql)
print(list(repo.cursor))


sql = [("40", "word1", "w1, w8, w9, w10"),
       ("45", "word2", "w4, w7, w5")]

repo.cursor.executemany("INSERT INTO lemma VALUES (%s, %s, %s)", sql)


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
            print(line.sense, line.surface, line.definition, line.examples)'''
