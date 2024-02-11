

import bisect

class SORTracker:

    def __init__(self):
        self.calls = 0
        self.data = []

    def add(self, name: str, score: int) -> None:
        index = bisect.bisect_left(self.data, (-score, name))
        self.data.insert(index, (-score, name))

    def get(self) -> str:
        ret = self.data[self.calls]
        self.calls += 1
        return ret[1]
