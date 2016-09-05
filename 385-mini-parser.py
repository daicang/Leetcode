class NestedInteger(object):
    def __init__(self, i):
        pass

    def add(self, obj):
        pass


class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        def _list(s, head):
            return s[head] == '['

        def _int(s, head):
            return not _list(s, head)

        def _parse_int(s, head, tail):
            if s[head:tail]:
                return NestedInteger(int(s[head:tail]))
            return NestedInteger()

        def _find_list_tail(s, head, tail):
            idx = head
            lparen = 0
            while idx < tail:
                ch = s[idx]
                if ch == '[':
                    lparen += 1
                elif ch == ']':
                    lparen -= 1
                elif ch == ',' and lparen == 0:
                    break
                idx += 1
            return idx

        def _find_int_tail(s, head, tail):
            while head < tail and s[head] == '-' or s[head].isdigit():
                head += 1
            return head

        def _parse(s, head, tail):
            if _int(s, head):
                return _parse_int(s, head, tail)

            root = NestedInteger()
            head += 1
            tail -= 1

            while head < tail:
                if _int(s, head):
                    int_tail = _find_int_tail(s, head, tail)
                    root.add(_parse_int(s, head, int_tail))
                    head = int_tail + 1
                else:
                    list_tail = _find_list_tail(s, head, tail)
                    root.add(_parse(s, head, list_tail))
                    head = list_tail + 1

            return root

        return _parse(s, 0, len(s))
