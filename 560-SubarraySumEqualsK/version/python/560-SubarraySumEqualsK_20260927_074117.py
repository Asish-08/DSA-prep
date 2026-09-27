# Last updated: 9/27/2026, 7:41:17 AM
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
20        # ans=0
21        # cursum=0
22        # h_map={0:1}
23        # for i in nums:
24        #     cursum+=i
25        #     diff=cursum-k
26        #     # Add the number of previous prefix sums equal to (cursum - k), since each forms a subarray ending here with sum k
27        #     ans+=h_map.get(diff,0)
28        #     # Store how many times the current prefix sum has appeared for future subarray checks
29        #     h_map[cursum]=1+h_map.get(cursum,0)
30        # return ans
31
32        ans=0
33        h_map={0:1}
34        cursum=0
35        for i in nums:
36            cursum+=i
37            diff=cursum-k
38            ans+=h_map.get(diff,0)
39            h_map[cursum]=1+h_map.get(cursum,0)
40        return ans
41        
42        
43