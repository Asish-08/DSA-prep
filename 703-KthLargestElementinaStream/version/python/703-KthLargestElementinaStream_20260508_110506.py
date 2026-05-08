# Last updated: 5/8/2026, 11:05:06 AM
1class KthLargest:
2
3    def __init__(self, k: int, nums: List[int]):
4        #contructing the minHeap
5        self.minHeap,self.k=nums,k
6        heapq.heapify(self.minHeap)
7        while len(self.minHeap)>k:
8            heapq.heappop(self.minHeap)
9
10    def add(self, val: int) -> int:
11        heapq.heappush(self.minHeap,val)
12        if len(self.minHeap)>self.k:
13            heapq.heappop(self.minHeap)
14        return self.minHeap[0]
15        
16
17
18# Your KthLargest object will be instantiated and called as such:
19# obj = KthLargest(k, nums)
20# param_1 = obj.add(val)