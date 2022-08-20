
from collections import defaultdict
from typing import List


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.pos = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.pos[word].append(i)


    def shortest(self, word1: str, word2: str) -> int:
        loc1 = self.pos[word1]
        loc2 = self.pos[word2]

        i1 = 0
        i2 = 0

        shortest = abs(loc1[0] - loc2[0])

        while i1 < len(loc1) and i2 < len(loc2):
            shortest = min(shortest, abs(loc1[i1]-loc2[i2]))
            if loc1[i1] < loc2[i2]:
                i1 += 1
            else:
                i2 += 1

        return shortest

inputs = [
    [["practice","makes","perfect","coding","makes"],[["coding","practice"],["makes","coding"]]],
]


for i in inputs:
    wd = WordDistance(i[0])
    for arg in i[1]:
        print(wd.shortest(*arg))
