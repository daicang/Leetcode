import random
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    _largesize = 300

    def __init__(self, head):
        self.head = head
        self.lsize = 0
        while head.next:
            head = head.next
            self.lsize += 1

        self.m1_idx = None
        self.m2_idx = None
        if self.lsize > self._largesize:
            self.m1_idx = self.lsize / 3   # start from 1/3
            self.m1 = self._getN(self.m1_idx)
            self.m2_idx = self.m1_idx * 2  # start from 2/3
            self.m2 = self._getN(self.m2_idx)

    def _getN(self, n):
        n -= 1
        p = self.head
        while n:
            p = p.next
            n -= 1
        return p

    def getRandom(self):
        def _get(delta, start):
            p = start
            while delta:
                p = p.next
                delta -= 1
            return p.val

        nextpos = random.randint(0, self.lsize)
        if not self.m1_idx:
            return _get(nextpos, self.head)

        if nextpos < self.m1_idx:
            val = _get(nextpos, self.head)
        elif nextpos < self.m2_idx:
            val = _get(nextpos - self.m1_idx, self.m1)
        else:
            val = _get(nextpos - self.m2_idx, self.m2)
        return val
