class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        size = len(mat)
        candidate = 1
        indexes = [0] * size

        while True:
            candidate_changed = False

            for i, index in enumerate(indexes):
                arr = mat[i]
                while index < len(arr) and arr[index] < candidate:
                    index += 1

                if index == len(arr):
                    return -1

                if arr[index] > candidate:
                    candidate = arr[index]
                    candidate_changed = True

                indexes[i] = index

            if candidate_changed is False:
                return candidate


s = Solution()

inputs = [
    [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]],
    [[1,2,3,4,7],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]],
]

for i in inputs:
    print s.smallestCommonElement(i)
