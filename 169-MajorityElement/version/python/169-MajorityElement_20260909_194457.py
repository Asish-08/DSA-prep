# Last updated: 9/9/2026, 7:44:57 PM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        # nums_map=Counter(nums)
4        # for key,val in nums_map.items():
5        #     if val>len(nums)/2:
6        #         return key
7        # return 0
8        # nums.sort()
9        # return nums[len(nums)//2] 
10        
11        # the num with highest freq will atleast reside at n//2th place
12        nums_map=Counter(nums)
13        heap=[]
14        for key,val in nums_map.items():
15            heapq.heappush(heap,[-val,key])
16        
17        res=heapq.heappop(heap)
18        return res[1]