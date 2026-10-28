# Last updated: 10/27/2026, 6:01:55 PM
1class Solution:
2    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
3        arr.sort()
4        diff=arr[1]-arr[0]
5        for i in range(2,len(arr)):
6            if diff== (arr[i]-arr[i-1]):
7                continue
8            else:
9                return False
10        return True
11            