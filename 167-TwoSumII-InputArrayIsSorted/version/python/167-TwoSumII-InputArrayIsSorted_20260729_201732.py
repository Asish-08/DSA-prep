# Last updated: 7/29/2026, 8:17:32 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        l,r=0,len(numbers)-1
4        while l<r:
5            total=numbers[l]+numbers[r]
6            if total>target:
7                r-=1
8            elif total<target:
9                l+=1
10            else:
11                return [l+1,r+1]