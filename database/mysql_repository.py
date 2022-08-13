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
        #self.cursor.close() I think this was a casualty of switching to mysql 8.0
        self.connection.close()

    def load_lemmas(self):
        sql = ('SELECT * '
               'FROM lemma '
               )
        self.cursor.execute(sql)
        all_lemmas = list(self.cursor)
        tokenized = []
        for lemma in all_lemmas:
            tokens = re.findall('\w+', lemma[2])
            tokenized.append((lemma[0], lemma[1], tokens))
        return tokenized


    def load_vectors(self):
        sql = ('SELECT * '
               'FROM vectors '
               )
        self.cursor.execute(sql)
        allvectors = list(self.cursor)  # NOTE, the answer from the cursor is given only ONCE!
        dictvectors = {}
        for vector in allvectors:
            separated = re.split(', ', vector[2])
            reconstituted = []
            for i, value in enumerate(separated):
                if i % 2 == 1:
                    if len(value) != 1:
                        value = 1
                    reconstituted.append((separated[i - 1], int(value)))
            dictvectors[vector[0]] = reconstituted
        return dictvectors

    def load_context_sent(self):
        sql = ('SELECT * '
               'FROM context_sentences '
               )
        self.cursor.execute(sql)
        allcs = list(self.cursor)
        contextsents = []
        for cs in allcs:
            reconstituted = []
            recon_words = re.findall('[a-z]+', cs[3])
            recon_nums = re.findall('[0-9]+', cs[3])
            # assert len(recon_words) == len(recon_nums)
            for i in range(len(recon_nums)):
                reconstituted.append((recon_words[i], int(recon_nums[i])))
            contextsents.append((cs[0], cs[2], reconstituted, recon_words))
        return contextsents

    def load_lexicon(self):
        sql = ('SELECT * '
               'FROM lexicon '
               )
        self.cursor.execute(sql)
        lexdraw = list(self.cursor)
        lexicon = {}
        for lex in lexdraw:
            word = re.findall('[a-z]+', lex[1])
            indices = re.findall('[0-9]+', lex[2])
            lexicon[word[0]] = indices
        return lexicon


