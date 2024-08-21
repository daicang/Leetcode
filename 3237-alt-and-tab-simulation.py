class Solution:
    def simulationResult(self, windows: List[int], queries: List[int]) -> List[int]:
        result = []
        moved = set()
        for q in queries[::-1]:
            if q not in moved:
                moved.add(q)
                result.append(q)

        for i in windows:
            if i not in moved:
                result.append(i)

        return result