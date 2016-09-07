import random


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val2idxs = {}
        self.vals = []
        self.counter = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        idx = len(self.vals)
        self.vals.append(val)
        self.counter += 1

        if val not in self.val2idxs:
            self.val2idxs[val] = [idx]
            firstappear = True
        else:
            self.val2idxs[val].append(idx)
            firstappear = False
        return firstappear

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.val2idxs:
            self.vals.remove(val)
            self.counter -= 1

            if len(self.val2idxs[val]) == 1:
                del self.val2idxs[val]
            else:
                self.val2idxs[val] = self.val2idxs[val][1:]
            removed = True
        else:
            removed = False

        return removed

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.vals)
