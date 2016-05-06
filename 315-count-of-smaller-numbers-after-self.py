# 315-count-of-smaller-numbers-after-self.py
# Difficulty: hard

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def mergesort(arr):
            l = len(arr)
            if l < 2: return arr
            mid = l / 2
            left, right = mergesort(arr[:mid]), mergesort(arr[mid:])

            for i in range(l)[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    arr[i] = left.pop()
                else:
                    arr[i] = right.pop()

            return arr
            
        smaller = [0] * len(nums)
        mergesort(list(enumerate(nums)))

        return smaller

s = Solution()
print s.countSmaller([5,2,0,1,3])
