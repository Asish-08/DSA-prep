# Last updated: 7/29/2026, 8:09:52 PM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        p1,p2=m-1,n-1
7        for p in range(m+n-1,-1,-1):
8            if p2<0:
9                break
10            if p1>=0 and nums1[p1]>nums2[p2]:
11                nums1[p]=nums1[p1]
12                p1-=1
13            else:
14                nums1[p]=nums2[p2]
15                p2-=1
16        
17