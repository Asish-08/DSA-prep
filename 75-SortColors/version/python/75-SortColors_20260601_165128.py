# Last updated: 6/1/2026, 4:51:28 PM
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        """
4        Dutch National Flag problem solution.
5        """
6        # For all idx < p0 : nums[idx < p0] = 0
7        # curr is an index of elements under consideration
8        p0 = curr = 0
9
10        # For all idx > p2 : nums[idx > p2] = 2
11        p2 = len(nums) - 1
12
13        while curr <= p2:
14            if nums[curr] == 0:
15                nums[p0], nums[curr] = nums[curr], nums[p0]
16                p0 += 1
17                curr += 1
18            elif nums[curr] == 2:
19                nums[curr], nums[p2] = nums[p2], nums[curr]
20                p2 -= 1
21            else:
22                curr += 1