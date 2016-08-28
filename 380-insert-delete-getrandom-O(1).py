class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.dsize = 0
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d.keys():
            return False
        self.d[val] = 1
        self.dsize += 1
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d.keys():
            del self.d[val]
            self.dsize -= 1
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randint(0, self.dsize-1)
        return self.d.keys()[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
