from collections import deque

class MedianFinder:

    def __init__(self):
        self.count = 0
        self.begin_index = 0
        self.arr = deque()


    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.count += 1
        if self.count > 1 and self.count % 2 == 1:
            self.arr.popleft()



    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return (self.arr[0]+self.arr[1])/2
        return self.arr[0]





# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()