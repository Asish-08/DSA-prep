# Last updated: 8/27/2026, 10:51:53 AM
1class Solution:
2    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
3        def slide(intervals):
4            intervals.sort()
5
6            n=len(intervals)
7            ans=0
8            window_sum=0
9            j=0
10
11            for i in range(n):
12                left=intervals[i][0]
13                right=left+k-1
14
15                #adding the intervals inside the window
16                while j<n and intervals[j][1]<=right:
17                    l,r,c=intervals[j]
18                    window_sum+=(r-l+1)*c
19                    j+=1
20                #add the partailly covered window to total
21                total=window_sum
22
23                #calclating if there is any overlap
24                if j<n and intervals[j][0]<=right:
25                    l,r,c=intervals[j]
26                    overlap=right-l+1
27                    total+=overlap*c
28                
29                ans=max(ans,total)
30                l,r,c=intervals[i]
31                window_sum-=(r-l+1)*c
32            return ans
33
34        ans1=slide(coins)
35        reversed_coins=[[-r,-l,c] for l,r,c in coins]
36        ans2=slide(reversed_coins)
37        return max(ans1,ans2)