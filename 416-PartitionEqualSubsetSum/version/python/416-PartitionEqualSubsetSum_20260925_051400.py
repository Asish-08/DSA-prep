# Last updated: 9/25/2026, 5:14:00 AM
1class Solution:
2    def canPartition(self, nums: list[int]) -> bool:
3        total=sum(nums)
4        if total%2!=0:      #odd total cannot split the nums equally
5            return False
6        target=total//2
7        dp={0}
8
9        for num in nums:
10            new_dp=dp.copy()
11            for n in dp:
12                new_sum=n+num
13                if new_sum== target:
14                    return True
15                elif new_sum < target:
16                    new_dp.add(new_sum)
17                dp=new_dp
18        return target in dp