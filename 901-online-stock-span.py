class StockSpanner:

    def __init__(self):
        self.i = 0
        self.stack = []

    def next(self, price: int) -> int:
        self.i += 1
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()
        if not self.stack:
            starti = 0
        else:
            starti = self.stack[-1][0]
        self.stack.append((self.i, price))
        return self.i - starti
