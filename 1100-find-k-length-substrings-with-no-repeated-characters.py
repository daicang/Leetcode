class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        count = 0
        counter = {}

        for i, val in enumerate(s):
            # move front pointer
            if val not in counter:
                counter[val] = 1
            else:
                counter[val] += 1
            # move back pointer if possible
            bi = i-k
            if bi >= 0:
                counter[s[bi]] -= 1
                if counter[s[bi]] == 0:
                    del counter[s[bi]]
            # check length
            if len(counter) == k:
                count += 1

        return count





        return maxlen
