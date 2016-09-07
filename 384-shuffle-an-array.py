# Fisher-Yates shuffle
import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type size: int
        """
        self.orig = nums
        self.shuf = [x for x in nums]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.orig

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in xrange(len(self.shuf)):
            j = random.randint(0, i)
            self.shuf[i], self.shuf[j] = self.shuf[j], self.shuf[i]

        return self.shuf
