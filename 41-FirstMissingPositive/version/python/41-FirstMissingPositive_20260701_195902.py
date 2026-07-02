# Last updated: 7/1/2026, 7:59:02 PM
1class Solution:
2    def firstMissingPositive(self, nums: List[int]) -> int:
3        # Example: nums = [3, 4, -1, 1], n = 4
4
5        # Step 1: Replace all numbers that are out of the range [1, n]
6        # with n + 1, since they cannot affect the answer.
7        # [3, 4, -1, 1] -> [3, 4, 5, 1]
8        for index in range(len(nums)):
9            if nums[index]<=0 or nums[index]>len(nums):
10                nums[index]=len(nums)+1
11
12        # Step 2: Use the index as a marker. For each value x in the array,
13        # if 1 <= x <= n, mark index (x - 1) as visited by making it negative.
14        # [3, 4, 5, 1] -> [-3, 4, -5, -1]
15        for num in nums:
16            num=abs(num)
17            if num<=len(nums) and nums[num-1]>0:
18                nums[num-1]=nums[num-1]*-1
19
20        # Step 3: Traverse the array and find the first positive index.
21        # The answer is (index + 1).
22        # Here, index 1 is positive, so the first missing positive is 2.
23        for index in range(len(nums)):
24            if nums[index]>0:
25                return index+1
26        return len(nums)+1
27