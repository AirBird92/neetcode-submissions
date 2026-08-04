class Twitter:

    def __init__(self):
        self.twits = defaultdict(list)
        self.follows = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twits[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.follows[userId]
        if userId not in followees:
            followees.add(userId)
        heap = []
        for followee in followees:
            for twit in self.twits[followee]:
                heapq.heappush(heap, twit)
                if len(heap) > 10:
                    heapq.heappop(heap)
        return [heapq.heappop(heap)[1] for _ in range(len(heap))][::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follows[followerId]:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)