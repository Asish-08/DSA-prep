# Last updated: 5/8/2026, 12:37:54 PM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        minHeap=[]
4        for i in nums:
5            heapq.heappush(minHeap,i)
6            if len(minHeap)>k:
7                heapq.heappop(minHeap)
8        return minHeap[0]
9            