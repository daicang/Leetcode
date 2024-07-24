class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        count = 0
        last_ch = None

        def save_compressed(i, ch, count):
            if ch is None:
                return i
            chars[i] = ch
            i += 1
            if count > 1:
                for c in str(count):
                    chars[i] = c
                    i += 1
            return i

        for ch in chars:
            if ch == last_ch:
                # add count
                count += 1
            else:
                # save last char with count
                i = save_compressed(i, last_ch, count)
                # set new char
                last_ch = ch
                count = 1

        i = save_compressed(i, last_ch, count)
        return i