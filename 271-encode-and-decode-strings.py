
from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = []
        for s in strs:
            encoded.append('%s ' % len(s))
            encoded.append(s)
        return ''.join(encoded)


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        i = 0
        while i < len(s):
            l = 0
            # scan length
            while s[i].isdigit():
                l *= 10
                l += int(s[i])
                i += 1

            # skip blank
            i += 1

            # scan str
            print(s[i])
            result.append(s[i:i+l])
            i += l

        return result

codec = Codec()
print(codec.decode(codec.encode(['hello', 'world'])))