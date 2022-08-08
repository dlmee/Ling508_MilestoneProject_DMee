from model.senses import *
import numpy as np

'''('animals', 'an', 'heart, earth, great, wallowing, mass, blood, hearts, men, glowing,
 hot, melted, metals, stones, ever, heard, philosophers, say, another, thing, greatest,
  consequence, take, care, go, hill, country, many, actually, lives, going, beasts, yet,
   fresh, animal, came, seemed, reasoned, certainly, fought, overcome, lina, last, wood,
    followed, forty, nine, grotesquely, ugly, extravagantly, abnormal, imagination, conceive, knew, bo'),'''

class SenseDistributor:

    def __init__(self, target, context): #target equals one vector, context equals all vectors.
        self.senses = self.groupings(target, context)
        self.probabilities = self.groupings(target, context)

    def groupings(self, target, context):
        allprobs = []
        for pair in context[target]:
            allprobs.append(pair[0])
            for pair2 in context[target]:
                if pair != pair2:
                    array1, array2 = self.vect_to_num(context[pair[0]], context[pair2[0]])
                    probability = self.cosine(array1, array2)
                    allprobs.append(probability)
        return allprobs
        #for vector bit in target
            #get vector of vector bit
            #compare that vector bit against every other vector bit
            #find the mathematically lowest difference among all possibilities.
            #produce senses based on these mathematically lowest clusters.

    def cosine(self, array1, array2):
        numerator = sum(array1 * array2)
        # print(numerator)
        denominator = sum(array1 ** 2) ** .5 * sum(array2 ** 2) ** .5
        # print(denominator)
        if numerator and denominator != 0:
            return numerator / denominator
        else:
            return 0

    def vect_to_num(self, vect1, vect2):
        # Should be receiving a list of tups (word, count)
        v1dict = {}
        v2dict = {}

        for pair1 in vect1:
            v1dict[pair1[0]] = pair1[1]
            v2dict[pair1[0]] = 0

        for pair2 in vect2:
            if pair2[0] in v2dict:
                v2dict[pair2[0]] += pair2[1]
            else:
                v2dict[pair2[0]] = pair2[1]
            if pair2[0] not in v1dict:
                v1dict[pair2[0]] = 0

        v1list = list(v1dict.items())
        v2list = list(v2dict.items())
        assert len(v1list) == len(v2list)

        v1list.sort(key=lambda x: x[
            0])  # MUST sort alphabetical, it would be a dreadful mistake to do it by their respective values.
        v2list.sort(key=lambda x: x[0])

        v1array = np.zeros(len(v1list))
        v2array = np.zeros(len(v2list))

        for i in range(len(v1list)):
            v1array[i] = v1list[i][1]
            v2array[i] = v2list[i][1]

        return v1array, v2array








