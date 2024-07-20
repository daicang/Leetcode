class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        rounds = min(x, y//4)
        if rounds % 2 == 1:
            return 'Alice'
        return 'Bob'
