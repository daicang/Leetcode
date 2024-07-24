class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        limit = max(candies) - extraCandies
        return [x>=limit for x in candies]
