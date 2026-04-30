# Last updated: 4/29/2026, 7:13:43 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        A,B=nums1,nums2
4        if len(A)>len(B):
5            A,B=B,A
6        l,r=0,len(A)-1
7        total=(len(nums1)+len(nums2))
8        half=total//2
9        while True:
10            i=(l+r)//2
11            j= half-i-2
12            Aleft= A[i] if i >=0 else float('-infinity')
13            Aright=A[i+1] if (i+1)<len(A) else float('infinity')
14            Bleft=B[j] if j >=0 else float('-infinity')
15            Bright=B[j+1] if (j+1)<len(B) else float('infinity')
16            if Aleft<=Bright and Bleft<=Aright:
17                if total%2:
18                    return min(Aright,Bright)
19                return (max(Aleft,Bleft)+min(Aright,Bright))/2
20            elif Aleft>Bright:
21                r=i-1
22            else:
23                l=i+1