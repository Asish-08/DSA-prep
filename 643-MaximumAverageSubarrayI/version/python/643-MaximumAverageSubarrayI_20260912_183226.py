# Last updated: 9/12/2026, 6:32:26 PM
1class Solution:
2    def findMaxAverage(self, nums: List[int], k: int) -> float:
3        curr_sum=sum(nums[:k])
4        max_sum=curr_sum
5        for i in range(k,len(nums)):
6            curr_sum=curr_sum+nums[i]-nums[i-k]
7            if curr_sum>max_sum:
8                max_sum=curr_sum
9        return max_sum/k
10
11
12
13        # curr_sum=sum(nums[:k])
14        # max_sum=curr_sum
15
16        # for i in range(k,len(nums)):
17        #     curr_sum=curr_sum+nums[i]-nums[i-k]
18        #     if curr_sum>max_sum:
19        #         max_sum=curr_sum
20        # return max_sum/k