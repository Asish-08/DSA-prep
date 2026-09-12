# Last updated: 9/12/2026, 10:54:41 AM
1class Solution:
2    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
3        def slide(intervals):
4            window_sum,ans,j=0,0,0
5            n=len(intervals)
6            intervals.sort()
7
8            for i in range(n):
9                left=intervals[i][0]
10                right=left+k-1
11
12                #whole window is covered
13                while j<n and intervals[j][1]<=right:
14                    l,r,c=intervals[j]
15                    window_sum+=(r-l+1)*c
16                    j+=1
17                
18                #adding the partial to total
19                total=window_sum
20
21                #checking if there is any overlap
22                if j<n and intervals[j][0]<=right:
23                    l,r,c=intervals[j]
24                    overlap=right-l+1
25                    total+=overlap*c
26                
27                ans=max(ans,total)
28                l,r,c=intervals[i]
29                
30                window_sum-=(r-l+1)*c
31            return ans
32
33        ans1=slide(coins)
34        reversed_coins=[(-r,-l,c) for l,r,c in coins]
35        ans2=slide(reversed_coins)
36        return max(ans1,ans2)
37
38
39        # def slide(intervals):
40        #     intervals.sort()
41
42        #     n=len(intervals)
43        #     ans=0
44        #     window_sum=0
45        #     j=0
46
47        #     for i in range(n):
48        #         left=intervals[i][0]
49        #         right=left+k-1
50
51        #         #adding the intervals inside the window
52        #         while j<n and intervals[j][1]<=right:
53        #             l,r,c=intervals[j]
54        #             window_sum+=(r-l+1)*c
55        #             j+=1
56        #         #add the partailly covered window to total
57        #         total=window_sum
58
59        #         #calclating if there is any overlap
60        #         if j<n and intervals[j][0]<=right:
61        #             l,r,c=intervals[j]
62        #             overlap=right-l+1
63        #             total+=overlap*c
64                
65        #         ans=max(ans,total)
66        #         l,r,c=intervals[i]
67        #         window_sum-=(r-l+1)*c
68        #     return ans
69
70        # ans1=slide(coins)
71        # reversed_coins=[[-r,-l,c] for l,r,c in coins]
72        # ans2=slide(reversed_coins)
73        # return max(ans1,ans2)