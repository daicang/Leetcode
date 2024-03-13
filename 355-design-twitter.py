

import heapq

class User:

    def __init__(self, uid):
        self.uid = uid
        self.follows = set()
        self.follows.add(self.uid)
        self.tweets = []

    def follow(self, uid):
        self.follows.add(uid)

    def unfollow(self, uid):
        if uid in self.follows:
            self.follows.remove(uid)

    def post(self, tid, timestamp):
        self.tweets.append(Tweet(tid, timestamp, len(self.tweets)))

class Tweet:

    def __init__(self, tid, timestamp, idx):
        self.tid = tid
        self.timestamp = timestamp
        self.index = idx


class Twitter:

    def __init__(self):
        self.users = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = User(userId)
        self.timestamp += 1
        self.users[userId].post(tweetId, self.timestamp)

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        user = self.users.get(userId)
        if not user:
            return []
        h = []
        for fid in user.follows:
            fo = self.users[fid]
            if fo.tweets:
                tw = fo.tweets[-1]
                heapq.heappush(h, (-tw.timestamp, tw.tid, fo, tw.index))

        while h and len(feed) < 10:
            _, tid, fo, index = heapq.heappop(h)
            feed.append(tid)
            if index > 0:
                index -= 1
                tw = fo.tweets[index]
                heapq.heappush(h, (-tw.timestamp, tw.tid, fo, tw.index))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
        self.users[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
        self.users[followerId].unfollow(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)