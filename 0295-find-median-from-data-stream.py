import heapq

class MedianFinder:

    def __init__(self):
        # Lower half
        self.max_heap = []
        # Higher half
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == 0 or num < -1*self.max_heap[0]:
            # Put to left
            heapq.heappush(self.max_heap, -num)
        else:
            # Put to right
            heapq.heappush(self.min_heap, num)

        # Rebalance
        if len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(self.min_heap, -1*heapq.heappop(self.max_heap))

        if len(self.min_heap) - len(self.max_heap) >= 1:
            heapq.heappush(self.max_heap, -1*heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # print(self.max_heap, self.min_heap)
        if len(self.max_heap) == len(self.min_heap):
            elem1 = -1 * self.max_heap[0]
            elem2 = self.min_heap[0]
            return (elem1 + elem2) / 2

        assert len(self.max_heap) - len(self.min_heap) == 1
        return -1 * self.max_heap[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(2)
# print(obj.findMedian())
# obj.addNum(3)
# print(obj.findMedian())


obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())