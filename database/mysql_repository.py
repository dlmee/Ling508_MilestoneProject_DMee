from database.repository import *
import mysql.connector


class MysqlRepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost', # to run LOCALLY, this should be localhost
            'port': '32000', # to run LOCALLY, this should be 32000
            'database': 'mcdonald',
            'autocommit': True
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        #self.cursor.close()
        self.connection.close()

    def load_lemmas(self):
        pass

    def load_vectors(self):
        pass
