# Last updated: 5/8/2026, 11:33:59 AM
1class Solution:
2    def lastStoneWeight(self, stones: List[int]) -> int:
3        stones=[-stone for stone in stones]
4        while len(stones)>1:
5            heapq.heapify(stones)
6            first=heapq.heappop(stones)
7            second=heapq.heappop(stones)
8            if second>first:
9                heapq.heappush(stones, first-second)
10        stones.append(0)
11        return abs(stones[0])