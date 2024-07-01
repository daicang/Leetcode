from typing import List


class Solution:
    def hIndex_sort(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i, c in enumerate(citations):
            # cites going down, papers(i+1) going up
            if c < i+1:
                return i
        # all cites are larger than papers
        return len(citations)

    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        ccount = [0] * (n+1)
        for c in citations:
            ccount[min(c, n)] += 1

        # ccount[i] is papers has cite == i
        papers = 0
        for cites in range(n, 0, -1):
            # cites going down
            # papers going up
            papers += ccount[cites]
            if papers >= cites:
                return cites

        return 0
