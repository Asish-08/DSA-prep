# Last updated: 10/12/2026, 3:46:38 PM
1class Solution:
2    def search(self, nums: list[int], target: int) -> bool:
3        low,high=0,len(nums)-1
4        while low<=high:
5            mid=(high+low)//2
6
7            if nums[mid]==target:
8                return True
9            
10            if nums[low]==nums[mid]==nums[high]:
11                low+=1
12                high-=1
13            
14            elif nums[low]<=nums[mid]:
15                if nums[low]<=target<nums[mid]:
16                    high=mid-1
17                else:
18                    low=mid+1
19            else:
20                if nums[mid]<target<=nums[high]:
21                    low=mid+1
22                else:
23                    high=mid-1
24        return False