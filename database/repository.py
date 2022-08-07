import abc
from model.lemmas import *
from model.vectors import *


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_lemmas(self): #  -> list[Word]
        raise NotImplementedError

    @abc.abstractmethod
    def load_vectors(self): #  -> list[Vector]
        raise NotImplementedError
