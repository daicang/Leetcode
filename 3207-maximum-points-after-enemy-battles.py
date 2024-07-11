class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyEnergies.sort()
        if currentEnergy < enemyEnergies[0]:
            return 0
        for i, val in enumerate(enemyEnergies):
            if i > 0:
                currentEnergy += val

        return currentEnergy // enemyEnergies[0]
