# Last updated: 8/27/2026, 4:13:20 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        l,r=0,len(numbers)-1
4        while l<=r:
5            total=numbers[l]+numbers[r]
6
7            if total>target:
8                r-=1
9            elif total<target:
10                l+=1
11            else:
12                return [l+1,r+1]