# 332-reconstruct-itinerary.py

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
# Wrong
        # ret = ["JFK"]
        # flag = 0
        # while flag == 0:
        #     tmp = "ZZZ"
        #     found = 0
        #     for curr in tickets:
        #         if curr[0] != ret[-1]: continue
        #         if curr[1] < tmp:
        #             tmp = curr[1]
        #             found = 1
        #     if found == 0: break
        #     if tmp in ret: flag = 1
        #     ret.append(tmp)

        # def minValue(l):
        #     ret = l[0]
        #     for i in l:
        #         if i < ret: ret = i
        #     return ret

        # dict = {}

        # for i in tickets:
        #     key, value = i[0], i[1]
        #     if key not in dict:
        #         dict[key] = [value]
        #     else:
        #         dict[key].append(value)

        # ret = ["JFK"]
        # flag = 0

        # while flag == 0:
        #     next = minValue(dict[ret[-1]])
        #     if next not in dict or next in ret: flag = 1
        #     ret.append(next)
            
        # return ret

        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a].append(b)
        ret, stack = [], ['JFK']
        while stack:
            while targets[stack[-1]]:
                stack.append(targets[stack[-1]].pop())
            ret.append(stack.pop())

        return ret[::-1]
