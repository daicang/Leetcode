class SparseVector:
    def __init__(self, nums: List[int]):
        self.vec = []
        self.n = len(nums)
        for i, n in enumerate(nums):
            if n != 0:
                self.vec.append((i, n))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        i = j = 0
        while i < len(self.vec) and j < len(vec.vec):
            v1 = self.vec[i]
            v2 = vec.vec[j]
            if v1[0] == v2[0]:
                product += v1[1] * v2[1]
                i += 1
                j += 1
            elif v1[0] < v2[0]:
                i += 1
            else:
                j += 1
        return product





# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)