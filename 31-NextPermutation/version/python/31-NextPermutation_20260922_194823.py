# Last updated: 9/22/2026, 7:48:23 PM
1class Solution:
2    def nextPermutation(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        #step-1 Find the first decreasing position from the right.
7        i=len(nums)-2
8        while i>=0 and nums[i]>=nums[i+1]:
9            i-=1
10        
11        #Step 2: Swap it with the next greater number.
12        if i>=0:
13            j=len(nums)-1
14            while nums[j]<=nums[i]:
15                j-=1
16            nums[i],nums[j]=nums[j],nums[i]
17        
18        #Step 3: Reverse the suffix to make it smallest.
19        l,r=i+1,len(nums)-1
20        while l<r:
21            nums[l],nums[r]=nums[r],nums[l]
22            l+=1
23            r-=1
24        
25
26
27        # #step-1
28        # i=len(nums)-2
29        # while i>=0 and nums[i]>=nums[i+1]:
30        #     i-=1
31        # #step-2
32        # if i>=0:
33        #     j=len(nums)-1
34        #     while nums[j]<=nums[i]:
35        #         j-=1
36        #     nums[i],nums[j]=nums[j],nums[i]
37        # #step-3
38        # l,r=i+1,len(nums)-1
39        # while l<r:
40        #     nums[l],nums[r]=nums[r],nums[l]
41        #     l+=1
42        #     r-=1
43        
44        