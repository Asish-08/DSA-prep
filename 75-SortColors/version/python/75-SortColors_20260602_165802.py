# Last updated: 6/2/2026, 4:58:02 PM
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        p0,curr=0,0
7        p2=len(nums)-1
8
9        while curr<=p2:
10            if nums[curr]==0:
11                nums[p0],nums[curr]=nums[curr],nums[p0]
12                curr+=1
13                p0+=1
14            elif nums[curr]==2:
15                nums[curr],nums[p2]=nums[p2],nums[curr]
16                # curr+=1
17                p2-=1
18            else:
19                curr+=1