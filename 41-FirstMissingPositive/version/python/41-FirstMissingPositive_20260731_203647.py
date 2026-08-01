# Last updated: 7/31/2026, 8:36:47 PM
1class Solution:
2    def firstMissingPositive(self, nums: List[int]) -> int:
3        # # Example: nums = [3, 4, -1, 1], n = 4
4
5        # # Step 1: Replace all numbers that are out of the range [1, n]
6        # # with n + 1, since they cannot affect the answer.
7        # # [3, 4, -1, 1] -> [3, 4, 5, 1]
8        # for index in range(len(nums)):
9        #     if nums[index]<=0 or nums[index]>len(nums):
10        #         nums[index]=len(nums)+1
11
12        # # Step 2: Use the index as a marker. For each value x in the array,
13        # # if 1 <= x <= n, mark index (x - 1) as visited by making it negative.
14        # # [3, 4, 5, 1] -> [-3, 4, -5, -1]
15        # for num in nums:
16        #     num=abs(num)
17        #     if num<=len(nums) and nums[num-1]>0:
18        #         nums[num-1]=nums[num-1]*-1
19
20        # # Step 3: Traverse the array and find the first positive index.
21        # # The answer is (index + 1).
22        # # Here, index 1 is positive, so the first missing positive is 2.
23        # for index in range(len(nums)):
24        #     if nums[index]>0:
25        #         return index+1
26        # return len(nums)+1
27
28        #read the comments above for clarity. below is only the code i practiced
29        for i in range(len(nums)):
30            if nums[i]<=0 or nums[i]>len(nums):
31                nums[i]=len(nums)+1
32        
33        for num in nums:
34            num=abs(num)
35            if num<=len(nums) and nums[num-1]>0:
36                nums[num-1]=nums[num-1]*-1
37        
38        for index in range(len(nums)):
39            if nums[index]>0:
40                return index+1
41        return len(nums)+1
42
43
44        
45    
46
47
48