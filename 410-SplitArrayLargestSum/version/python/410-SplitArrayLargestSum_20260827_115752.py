# Last updated: 8/27/2026, 11:57:52 AM
1class Solution:
2    def splitArray(self, nums: List[int], k: int) -> int:
3        def canSplit(largest):
4            curSum=0
5            arrayCount=0
6            for n in nums:
7                curSum+=n
8                if curSum>largest:
9                    arrayCount+=1
10                    curSum=n
11            return True if arrayCount+1<=k else False
12
13        l,r=max(nums),sum(nums)
14        result=r
15        while l<=r:
16            mid=(l+r)//2
17            if canSplit(mid):
18                result=mid
19                r=mid-1
20            else:
21                l=mid+1
22        return result
23