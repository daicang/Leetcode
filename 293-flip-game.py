class Solution:
    def generatePossibleNextMoves(self, arr: str) -> List[str]:
        n = len(arr)
        moves = []
        i = 0
        while i < n-1:
            if arr[i] == '+':
                if arr[i+1] == '+':
                    moves.append(arr[:i]+'--'+arr[i+2:])
                    i += 1
                else:
                    i += 2
            else:
                i += 1
        return moves
