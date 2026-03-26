# Last updated: 3/25/2026, 5:00:46 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        count=Counter(nums)
4        heap=[]
5        res=[]
6        for num,freq in count.items():
7            heap.append((-freq,num))
8        heapq.heapify(heap)
9
10        for _ in range(k):
11            freq,num=heapq.heappop(heap)
12            res.append(num)
13        return res
14
15