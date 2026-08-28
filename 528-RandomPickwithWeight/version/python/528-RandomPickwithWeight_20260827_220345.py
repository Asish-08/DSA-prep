# Last updated: 8/27/2026, 10:03:45 PM
1class Solution:
2
3    def __init__(self, w: List[int]):
4        self.prefix=[]
5        prefix_sum=0
6        for weight in w:
7            prefix_sum+=weight
8            self.prefix.append(prefix_sum)
9        self.total=prefix_sum
10
11    def pickIndex(self) -> int:
12        target=random.randint(1, self.total)
13        return bisect.bisect_left(self.prefix,target)
14        
15
16
17# Your Solution object will be instantiated and called as such:
18# obj = Solution(w)
19# param_1 = obj.pickIndex()