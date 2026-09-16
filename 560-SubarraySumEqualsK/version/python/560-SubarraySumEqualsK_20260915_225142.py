# Last updated: 9/15/2026, 10:51:42 PM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        # ans=0
4        # for i in range(len(nums)):
5        #     total=0
6        #     for end in range(i,len(nums)):
7        #         total+=nums[end]
8        #         if total==k:
9        #             ans+=1
10        # return ans.    #brutre force, TLE
11        # res=0
12        # curSum=0
13        # prefixSums={0:1}
14        # for n in nums:
15        #     curSum+=n
16        #     diff=curSum-k
17        #     res+=prefixSums.get(diff,0)
18        #     prefixSums[curSum]=1+prefixSums.get(curSum,0)
19        # return res
20        ans=0
21        h_map={0:1}
22        cursum=0
23        for i in nums:
24            cursum+=i
25            diff=cursum-k
26            ans+=h_map.get(diff,0)
27            h_map[cursum]=1+h_map.get(cursum,0)
28        return ans
29        
30