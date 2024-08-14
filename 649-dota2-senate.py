class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        rq = deque()
        dq = deque()

        for i, val in enumerate(senate):
            if val == 'R':
                rq.append(i)
            else:
                dq.append(i)

        while rq and dq:
            ri = rq.popleft()
            di = dq.popleft()

            if ri < di:
                rq.append(ri+n)
            else:
                dq.append(di+n)

        if rq:
            return 'Radiant'
        return 'Dire'
