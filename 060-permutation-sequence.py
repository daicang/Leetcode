class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorials = [1] * (n)

        for i in range(1, n):
            factorials[i] = factorials[i-1] * i

        result = ''
        nums = range(1, n+1)

        k -= 1
        for i in range(n-1, -1, -1):
            index = k / factorials[i]
            k -= factorials[i] * index
            result += str(nums[index])
            del nums[index]

        return result
        # Cannot use backtrack since it is not ordered
        # def backtrack(start):
        #     if start == n:
        #         print ''.join([str(i) for i in numbers])
        #         counter[0] += 1
        #         if counter[0] == k:
        #             counter[1] = ''.join([str(i) for i in numbers])
        #         return

        #     if counter[0] == k:
        #         return

        #     for i in range(start, n):
        #         numbers[start], numbers[i] = numbers[i], numbers[start]
        #         backtrack(start+1)
        #         numbers[start], numbers[i] = numbers[i], numbers[start]

        # backtrack(0)
        # return counter[1]


s = Solution()

inputs = [
    [3, 3],
    [3, 5],
    [4, 9]
]

for input in inputs:
    print(s.getPermutation(*input))
