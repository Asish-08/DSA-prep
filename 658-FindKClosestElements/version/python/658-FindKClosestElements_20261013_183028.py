# Last updated: 10/13/2026, 6:30:28 PM
1class Solution:
2    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
3        left,right=0,len(arr)-k
4        while left<right:
5            mid=(left+right)//2
6            if x-arr[mid]>arr[mid+k]-x:
7                left=mid+1
8            else:
9                right=mid
10        return arr[left:left+k]
11
12
13
14        
15
16