
import bisect
from collections import deque

from sortedcontainers import SortedList

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.q = deque()
        self.sorted = SortedList()
        self.first_k = 0
        self.last_k = 0
        self.sum = 0

    def addElement(self, num: int) -> None:
        self.sum += num
        self.q.append(num)

        index = self.sorted.bisect_left(num)
        if index < self.k:
            # insert low part
            self.first_k += num
            if len(self.sorted) >= self.k:
                # pop low part
                self.first_k -= self.sorted[self.k-1]

        # num can be in both low/high sum
        if index > len(self.sorted) - self.k:
            # insert high part
            self.last_k += num
            if len(self.sorted) >= self.k:
                # pop high part
                self.last_k -= self.sorted[-self.k]

        # insert sorted
        self.sorted.add(num)

        # pop leftmost element
        if len(self.q) > self.m:
            num = self.q.popleft()
            self.sum -= num

            index = self.sorted.index(num)
            if index < self.k:
                self.first_k -= num
                self.first_k += self.sorted[self.k]
            elif index > self.m - self.k:
                self.last_k -= num
                self.last_k += self.sorted[-self.k-1]
            self.sorted.remove(num)

    def calculateMKAverage(self) -> int:
        # Remove smallest and largets k elems from container
        # Calculate average, round to integer
        if len(self.sorted) < self.m:
            return -1
        return (self.sum - self.first_k - self.last_k) // (self.m - 2*self.k)



# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()