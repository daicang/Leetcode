class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if left:
            max_time = max(left)
        else:
            max_time = 0
        for r in right:
            max_time = max(max_time, n-r)
        return max_time
