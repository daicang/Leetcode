class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False

        # make sure s is shorter
        if len(s) > len(t):
            s, t = t, s

        s_idx = t_idx = 0
        while s_idx < len(s) and t_idx < len(t):
            if s[s_idx] != t[t_idx]:
                if s[s_idx+1:] == t[t_idx+1:]:
                    return True
                if s[s_idx:] == t[t_idx+1:]:
                    return True
                return False

            s_idx += 1
            t_idx += 1

        return len(t) > len(s)
        # return s_idx == len(s) and t_idx == len(t)


        # cache = {}

        # def edit_dist(m, n):
        #     if not m:
        #         return len(n)
        #     if not n:
        #         return len(m)
        #     if (m, n) in cache:
        #         return cache[(m, n)]

        #     if m[-1] == n[-1]:
        #         cache[(m,n)] = edit_dist(m[:-1], n[:-1])
        #     else:
        #         cache[(m,n)] = 1 + min(edit_dist(m[:-1], n[:-1]), edit_dist(m[:-1], n), edit_dist(m, n[:-1]))
        #     return cache[(m,n)]

        # return edit_dist(s, t) == 1

s = Solution()

data = [
    ["ab", "acb"],
    ["cab", "ad"],
    ["1203", "1213"],
    ["abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdef",
"bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg"],
]

for d in data:
    print(s.isOneEditDistance(*d))
