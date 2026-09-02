class Twitter:

    def __init__(self):
        self.followMap = {}
        self.tweetMap = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        if userId in self.tweetMap:
            self.tweetMap[userId].append((self.count, tweetId))
        else:
            self.tweetMap[userId] = []
            self.tweetMap[userId].append((self.count, tweetId))
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []

        if userId in self.tweetMap:
            tweets.extend(self.tweetMap[userId])

        for followee in self.followMap.get(userId, set()):
            if followee != userId and followee in self.tweetMap:
                tweets.extend(self.tweetMap.get(followee))
        
        tweets.sort(reverse=True)

        return [tweetId for _, tweetId in tweets[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].add(followeeId)
        else:
            self.followMap[followerId] = set()
            self.followMap[followerId].add(followeeId)

        return
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap.get(followerId):
            self.followMap[followerId].remove(followeeId)
        
        return
