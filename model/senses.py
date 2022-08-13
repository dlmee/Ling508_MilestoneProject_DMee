

class Senses:

    def __init__(self, target, sequence, subvect, contextsentences ):
        self.surface = target
        self.sense = sequence
        self.definition = subvect
        self.pos = "UNK"
        self.examples = contextsentences