class Leaderboard(object):

    def __init__(self):
        self.player_score = {}
        self.scores = []

    def _insert_score(self, new):
        for i, val in enumerate(self.scores):
            if val < new:
                self.scores.insert(i, new)
                return

        self.scores.append(new)

    def _remove_score(self, old):
        for i, val in enumerate(self.scores):
            if val == old:
                del self.scores[i]
                return


    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        if playerId not in self.player_score:
            self.player_score[playerId] = score

        else:
            self._remove_score(self.player_score[playerId])
            self.player_score[playerId] += score

        self._insert_score(self.player_score[playerId])


    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        K = min(K, len(self.scores))
        return sum(self.scores[:K])


    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        assert playerId in self.player_score
        self._remove_score(self.player_score[playerId])
        self.player_score[playerId] = 0



# Your Leaderboard object will be instantiated and called as such:
b = Leaderboard()

b.addScore(1,73)
b.addScore(2,56);   # leaderboard = [[1,73],[2,56]];
b.addScore(3,39);   # leaderboard = [[1,73],[2,56],[3,39]];
b.addScore(4,51);   # leaderboard = [[1,73],[2,56],[3,39],[4,51]];
b.addScore(5,4);    # leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
print b.top(1);     # 73
b.reset(1);         # leaderboard = [[2,56],[3,39],[4,51],[5,4]];
b.reset(2);         # leaderboard = [[3,39],[4,51],[5,4]];
b.addScore(2,51);   # leaderboard = [[2,51],[3,39],[4,51],[5,4]];
print b.top(3);     # returns 141 = 51 + 51 + 39;

# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)