class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Stack
        # Time: O(n*m)
        # Space: O(n)
        stack = []
        part = [ch for ch in part]
        for ch in s:
            stack.append(ch)
            if len(stack) >= len(part) and stack[-len(part):] == part:
                stack = stack[:-len(part)]
        return ''.join(stack)

    def removeOccurrences_kmp(self, s: str, part: str) -> str:
        # KMP matching
        def compute_longest_prefix_suffix(pattern):
            lps = [0] * len(pattern)
            curr = 1
            prefix_len = 0
            while curr < len(pattern):
                if pattern[curr] == pattern[prefix_len]:
                    # current ch matches
                    prefix_len += 1
                    lps[curr] = prefix_len
                    curr += 1
                elif prefix_len > 0:
                    # unmatch but previously matched, backtrack
                    prefix_len = lps[prefix_len-1]
                else:
                    lps[curr] = 0
                    curr += 1
            return lps

        # KMP longest prefix suffix
        lps = compute_longest_prefix_suffix(part)

        stack = []
        matches = [0] * (len(s)+1)  # match index

        si, pi = 0, 0

        while si < len(s):
            ch = s[si]

            if ch == part[pi]:
                stack.append(ch)
                if pi == len(part)-1:
                    # matches entire pattern
                    stack = stack[:-len(part)]
                    if stack:
                        pi = matches[len(stack)]
                    else:
                        pi = 0
                else:
                    pi += 1
                    matches[len(stack)] = pi

            else:
                if pi != 0:
                    # unmatch, try next suffix-prefix match
                    pi = lps[pi-1]
                    continue
                else:
                    stack.append(ch)
                    matches[len(stack)] = 0

            si += 1

        return ''.join(stack)
