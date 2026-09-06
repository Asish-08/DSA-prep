# Last updated: 9/6/2026, 7:13:12 AM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        # minHeap=[]
4        # for i in nums:
5        #     heapq.heappush(minHeap,i)
6        #     if len(minHeap)>k:
7        #         heapq.heappop(minHeap)
8        # return minHeap[0]
9        minheap=[]
10        for i in range(len(nums)):
11            heapq.heappush(minheap,[-nums[i],i])
12            
13
14        for i in nums:
15            while k>1:
16                heapq.heappop(minheap)
17                k-=1
18        return nums[minheap[0][1]]
19            
20
21