from typing import List

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max([len(w) for w in words])

        vert = []
        for _ in range(max_len):
            vert.append([])

        for word in words:
            for i in range(max_len):
                if i < len(word):
                    vert[i].append(word[i])
                else:
                    vert[i].append(' ')

        for i, s in enumerate(vert):
            s = ''.join(s)
            vert[i] = s.rstrip()

        return vert

s = Solution()

data = [
    "HOW ARE YOU",
    "TO BE OR NOT TO BE",
    "CONTEST IS COMING"
]

for d in data:
    print(s.printVertically(d))
