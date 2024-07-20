class Solution:
    def canWin(self, currentState: str) -> bool:
        counter = []
        c = 0
        for i, val in enumerate(currentState):
            if val == '+':
                c += 1
            if i == len(currentState)-1 or val == '-':
                if c > 1:
                    counter.append(c)
                c = 0

        cache = {}

        def win(counter):
            counter = [i for i in counter if i >= 2]
            counter.sort(reverse=True)
            if not counter:
                return False

            key = tuple(counter)
            if key in cache:
                return cache[key]

            for i, c in enumerate(counter):
                for j in range(c-1):
                    if win(counter[:i] + [j, c-j-2] + counter[i+1:]) is False:
                        cache[key] = True
                        return True

            cache[key] = False
            return False

        return win(counter)
