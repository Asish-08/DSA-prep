# Last updated: 8/29/2026, 12:28:19 PM
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(nums)):
            val = nums[right]
            freq[val] += 1

            while (freq[val] > k):
                freq[nums[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
        
        return max_len
