# DROP DATABASE IF EXISTS mcdonald;


from sqldatabase.mysql_repository import *

repo = MysqlRepository()


sql = ('SELECT * '
       'FROM lemma '
       )
repo.cursor.execute(sql)
print(list(repo.cursor))
'''
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
'''