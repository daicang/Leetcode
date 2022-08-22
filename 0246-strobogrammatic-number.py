class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        reverse_table = {
            0: 0,
            1: 1,
            2: None,
            3: None,
            4: None,
            5: None,
            6: 9,
            7: None,
            8: 8,
            9: 6,
        }

        lasti = len(num)-1

        for i, val in enumerate(num):
            j = len(num)-1-i
            if i > j:
                break

            v1 = int(val)
            v2 = int(num[j])
            if reverse_table[v1] != v2:
                return False

        return True