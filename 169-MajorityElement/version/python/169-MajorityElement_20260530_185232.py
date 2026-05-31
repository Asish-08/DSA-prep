# Last updated: 5/30/2026, 6:52:32 PM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        # nums_map=Counter(nums)
4        # for key,val in nums_map.items():
5        #     if val>len(nums)/2:
6        #         return key
7        # return 0
8        nums.sort()
9        return nums[len(nums)//2]