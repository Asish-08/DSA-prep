# Last updated: 9/6/2026, 7:16:40 AM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        minheap=[]
4        for i in nums:
5            heapq.heappush(minheap,i)
6            if len(minheap)>k:
7                heapq.heappop(minheap)
8        return minheap[0]
9        # minheap=[]
10        # for i in range(len(nums)):
11        #     heapq.heappush(minheap,[-nums[i],i])
12
13        # for i in nums:
14        #     while k>1:
15        #         heapq.heappop(minheap)
16        #         k-=1
17        # return nums[minheap[0][1]]
18            
19
20