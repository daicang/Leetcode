class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []

        def bisearch(s):
            lo, hi = 0, len(potions)-1

            while lo < hi:
                mid = (lo+hi) // 2
                if s * potions[mid] >= success:
                    hi = mid
                else:
                    lo = mid + 1

            if s * potions[lo] < success:
                return 0
            return len(potions) - lo

        for s in spells:
            result.append(bisearch(s))

        return result