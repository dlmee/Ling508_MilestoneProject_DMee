from database.mysql_repository import *
from database.repository import *

def test_SQLdatabase():
    repo = MysqlRepository()
    sql = ('SELECT COUNT(*) '
           'FROM lemma')
    repo.cursor.execute(sql)
    answer = (list(repo.cursor))
    assert answer[0][0] == 92