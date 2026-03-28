# Last updated: 3/28/2026, 1:42:48 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        l,r=0,len(numbers)-1
4        while l<r:
5            sum_num=numbers[l]+numbers[r]
6            if sum_num < target:
7                l+=1
8            if sum_num>target:
9                r-=1
10            if sum_num==target:
11                return [l+1,r+1]
12        return False
13