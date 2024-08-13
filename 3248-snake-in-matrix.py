class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        val = 0
        d = {
            'UP': -n,
            'DOWN': n,
            'LEFT': -1,
            'RIGHT': 1,
        }
        for cmd in commands:
            val += d[cmd]
        return val
