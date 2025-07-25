import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.time=0
        self.tweets=defaultdict(list)
        self.following=defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweets[userId].append((self.time,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        candidates=[]
        users_to_check=self.following[userId]|{userId}
        for u in users_to_check:
            for t in self.tweets[u][-10:]:
                candidates.append(t)
        return [tweetId for _,tweetId in heapq.nlargest(10, candidates)]

    def follow(self, followerId: int, followeeId: int) -> None:
         if followerId != followeeId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
         if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
