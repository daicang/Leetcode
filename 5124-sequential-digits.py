class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result = []

        def gen(width):
            nums = '123456789'
            for start in range(10-width):
                end = start + width
                yield int(nums[start:end])

        w1 = len(str(low))
        w2 = len(str(high))

        for w in range(w1, w2+1):
            for num in gen(w):
                if num > high:
                    break
                if num >= low:
                    result.append(num)

        return result


s = Solution()

data = [
    [100, 300],
    [1000, 13000]
]

for d in data:
    print s.sequentialDigits(*d)
