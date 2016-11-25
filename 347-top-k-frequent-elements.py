import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        bucket = [[] for x in nums]
        for key, freq in collections.Counter(nums).items():
            bucket[len(nums) - freq].append(key)
        return reduce(lambda x, y: x + y, bucket)[:k]

s = Solution()
print s.topKFrequent([1, 1, 2, 2, 1, 3], 2)
