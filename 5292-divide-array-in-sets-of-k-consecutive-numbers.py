class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) % k != 0:
            return False

        from collections import Counter
        counter = Counter(nums)
        nums = counter.keys()
        nums.sort()

        class Node(object):
            def __init__(self, val, count):
                self.val = val
                self.count = count
                self.next = None

        root = Node(None, None)
        last_node = root
        for n in nums:
            last_node.next = Node(n, counter[n])
            last_node = last_node.next

        while root.next:
            parent = root
            last_val = None
            for _ in range(k):
                curr = parent.next
                if curr is None:
                    return False

                if last_val is not None and curr.val != last_val + 1:
                    return False

                last_val = curr.val
                curr.count -= 1
                if curr.count == 0:
                    parent.next = curr.next
                else:
                    parent = curr

        return True


s = Solution()

data = [
    [[1,2,3,3,4,4,5,6], 4],
    [[3,2,1,2,3,4,3,4,5,9,10,11], 3],
    [[3,3,2,2,1,1], 3],
    [[1,2,3,4], 3]
]

for d in data:
    print s.isPossibleDivide(*d)

