from model.senses import *
import numpy as np

'''('animals', 'an', 'heart, earth, great, wallowing, mass, blood, hearts, men, glowing,
 hot, melted, metals, stones, ever, heard, philosophers, say, another, thing, greatest,
  consequence, take, care, go, hill, country, many, actually, lives, going, beasts, yet,
   fresh, animal, came, seemed, reasoned, certainly, fought, overcome, lina, last, wood,
    followed, forty, nine, grotesquely, ugly, extravagantly, abnormal, imagination, conceive, knew, bo'),'''

class SenseDistributor:

    def __init__(self, target, context): #target equals one vector, context equals all vectors.
        self.probabilities = self.groupings(target, context)
        self.senses = self.splitgroups(self.probabilities)

    def groupings(self, target, context):
        groupings = {}
        for pair in context[target]:
            numprobs = []
            allprobs = []
            vecroot = pair[0]
            for pair2 in context[target]:
                if pair != pair2:
                    array1, array2 = self.vect_to_num(context[pair[0]], context[pair2[0]])
                    probability = self.cosine(array1, array2)
                    probability = float(probability)
                    numprobs.append((pair2[0], probability))
            numprobs.sort(key=lambda x: x[1], reverse=True)
            groupings[vecroot] = numprobs
        return groupings
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



    def splitgroups(self, probabilities):
        copy = probabilities
        #for each dictionary element
            #search the key in the values of all the others.
            #create list with highest coindexed values
        sensegroups = []
        used = []
        for k, v in probabilities.items():
            grouping = [(k, 1)]
            if k not in used:
                for k2, v2 in copy.items():
                    #print("Same word? ", k, k2)
                    if k != k2: #not the same key
                        for step in v2:
                            if k == step[0]: #finding the right point in the list
                                similarity = step[1]
                                if similarity > .4:
                                    grouping.append((k2, 1)) #These keys share a high similarity
                                    used.append(k2)
            sensegroups.append(grouping)
        refinedgroups = self.splitrefine(sensegroups)
        #print("These are refined", refinedgroups)
        #return refinedgroups

    def removedoubles(self, blist):
        print("blist", blist)
        new = set(blist)
        slist = list(new)
        return slist
    def splitrefine(self, sensegroups): #receiving a list of a list of tuples.

        #Step one: weed out singletons
        rgroups1 = []
        for group in sensegroups:
            if len(group) > 2:
                rgroups1.append(group)
        #Step two: recursively merge as necessary.
        newgroupings = rgroups1
        print(newgroupings)
        for groupa in rgroups1:
            for groupb in rgroups1:
                if groupa != groupb:
                    aga, agb = self.vect_to_num(groupa, groupb)
                    cvalue = self.cosine(aga, agb)
                    if cvalue > .5:
                        merged = groupa, groupb
                        merged = self.removedoubles(merged)
                        newgroupings.remove(groupa)
                        newgroupings.remove(groupb)
                        newgroupings.append(merged)
                        print("These are the new groupings", newgroupings)
                        finalgroupings = self.splitrefine(newgroupings)
                        return finalgroupings
                    else:
                        return newgroupings


            #search rest of dict, excluding what has already been grouped
            #Create new list




