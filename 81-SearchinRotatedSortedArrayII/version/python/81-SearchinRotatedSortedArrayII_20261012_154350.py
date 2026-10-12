# Last updated: 10/12/2026, 3:43:50 PM
1class Solution:
2    def search(self, nums: list[int], target: int) -> bool:
3        low,high=0,len(nums)-1
4        while low<=high:
5            mid=(low+high)//2
6
7            if nums[mid]==target:
8                return True
9            
10            #duplicate edge case
11            if nums[low]==nums[mid]==nums[high]:
12                low+=1
13                high-=1
14            
15            #left half is soretd
16            elif nums[low]<=nums[mid]:
17                if nums[low]<=target<=nums[mid]:
18                    high=mid-1
19                else:
20                    low=mid+1
21            
22            #right half is sorted
23            else:
24                if nums[mid]<target<=nums[high]:
25                    low=mid+1
26                else:
27                    high=mid-1
28        return False
29            
30            