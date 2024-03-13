

from collections import defaultdict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.kv = {}
        self.k_to_freq = defaultdict(int)
        self.freq_to_k = defaultdict(set)

    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        self.increase_freq(key)
        return self.kv[key]

    def increase_freq(self, key):
        new_freq = self.k_to_freq[key] + 1
        self.k_to_freq[key] = new_freq
        self.freq_to_k[new_freq-1].remove(key)
        self.freq_to_k[new_freq].add(key)

    def remove_lfu(self):


    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            self.kv[key] = value
            self.increase_freq(key)
            return

        self.remove_lfu()
        self.kv[key] = value
        self.k_to_freq[key] = 1
        self.freq_to_k[1].add(key)



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)