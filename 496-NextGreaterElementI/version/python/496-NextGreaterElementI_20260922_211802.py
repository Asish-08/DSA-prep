# Last updated: 9/22/2026, 9:18:02 PM
1class Solution:
2    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
3        #O(n*m)
4
5        nums1Idx={n:i for i,n in enumerate(nums1)}
6        res=[-1]*len(nums1)
7
8        for i in range(len(nums2)):
9            if nums2[i] not in nums1Idx:
10                continue
11            else:
12                for j in range(i+1,len(nums2)):
13                    if nums2[j]>nums2[i]:
14                        idx=nums1Idx[nums2[i]]
15                        res[idx]=nums2[j]
16                        break
17        return res