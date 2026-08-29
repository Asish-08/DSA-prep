# Last updated: 8/29/2026, 1:04:24 PM
1class Solution:
2    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
3        left=0
4        satisfied=0
5        window,max_window=0,0
6
7        for right in range(len(customers)):
8            if grumpy[right]:
9                window+=customers[right]
10            else:
11                satisfied+=customers[right]
12
13            while right-left+1>minutes:
14                if grumpy[left]:
15                    window-=customers[left]
16                left+=1
17            max_window=max(max_window,window)
18        return satisfied+max_window