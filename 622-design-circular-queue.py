class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [None] * k
        self.k = k
        self.next = 0
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr[self.next] = value
        if self.tail is None:
            self.tail = self.next
        self.next = (self.next + 1) % self.k
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail + 1) % self.k
        if self.tail == self.next:
            self.tail = None
        return True

    def Front(self) -> int:
        if self.tail is None:
            return -1
        return self.arr[self.tail]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.next-1]

    def isEmpty(self) -> bool:
        return self.tail is None

    def isFull(self) -> bool:
        return self.next == self.tail



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()