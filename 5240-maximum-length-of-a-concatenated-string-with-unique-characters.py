class Solution(object):
    def __init__(self):
        self.max_len = 0

    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        unavail = []

        for i, word in enumerate(arr):
            mask = 0
            for ch in word:
                bitmap = 1 << (ord(ch)-ord('a'))
                if bitmap & mask:
                    unavail.append(i)
                    break
                mask |= bitmap

        arr = [w for i, w in enumerate(arr) if i not in unavail]
        masks = []

        def make_bit_mask(word):
            mask = 0
            for ch in word:
                bitmap = 1 << (ord(ch) - ord('a'))
                mask |= bitmap
            return mask


        for word in arr:
            masks.append(make_bit_mask(word))

        def recurse(index, mask, words):
            if index == len(arr):
                length = sum([len(w) for w in words])
                self.max_len = max(self.max_len, length)
                return

            # Skip this word
            recurse(index+1, mask, words)
            if masks[index] & mask == 0:
                # Include this word
                recurse(index+1, mask | masks[index], words+[arr[index]])

        recurse(0, 0, [])
        return self.max_len

s = Solution()
inputs = [
    ["yy","bkhwmpbiisbldzknpm"],
]

for i in inputs:
    print s.maxLength(i)

