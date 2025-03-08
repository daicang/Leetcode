import math
import random
import unittest

class MaxSegmentTree:
    '''
    Easy segment tree implementation
    Only support single update.
    Range update with cache would be complicated in this case, so not implemented

    See: https://codeforces.com/blog/entry/1256
    '''

    def __init__(self, n):
        self.n = n
        # Leaf starts at tree[self.n]
        # Tree starts at tree[1]
        # Child of tree[i] is tree[2*i] and tree[2*i+1]
        self.arr = [0] * (2*self.n)

    def build(self, arr):
        for i, val in enumerate(arr):
            self.arr[i+self.n] = val
        for i in range(self.n-1, 0, -1):
            # segment tree index begins at 1
            self.arr[i] = max(self.arr[i*2], self.arr[i*2+1])

    def query(self, l, r):
        '''Range query, both sides inclusive'''
        l += self.n
        r += self.n
        result = -math.inf

        while l <= r:
            if l & 1:
                result = max(result, self.arr[l])
            if r & 1 == 0:
                result = max(result, self.arr[r])
            l = (l+1) >> 1  # move right and up
            r = (r-1) >> 1  # move left and up
        return result

    def update(self, i, val):
        '''Update for single index'''
        i += self.n
        self.arr[i] = val
        while i > 1:
            i >>= 1
            self.arr[i] = max(self.arr[i*2], self.arr[i*2+1])


class TestSegmentTree(unittest.TestCase):

    test_cases = [2048, 10000]

    def test_build(self):
        for n in self.test_cases:
            print(f'Testing build tree: size: {n}')
            data = [random.randint(0, n) for _ in range(n)]
            tree = MaxSegmentTree(n)
            tree.build(data)

            for _ in range(300):
                left = random.randint(0, n-2)
                right = random.randint(left+1, n-1)
                self.assertEqual(tree.query(left, right),
                                 max(data[left:right+1]))

    def test_update(self):
        for n in self.test_cases:
            print(f'Testing range modify: size: {n}')
            data = [random.randint(0, n) for _ in range(n)]
            tree = MaxSegmentTree(n)
            tree.build(data)

            for _ in range(3000):
                i = random.randint(0, n-1)
                val = random.randint(0, n)

                data[i] = val
                tree.update(i, val)

                left = random.randint(0, i)
                right = random.randint(i, n-1)
                self.assertEqual(tree.query(left, right),
                                 max(data[left:right+1]))


if __name__ == '__main__':
    unittest.main()
