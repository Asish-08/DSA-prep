# Last updated: 9/25/2026, 6:26:13 PM
1class Solution:
2    def maxDistance(self, position: list[int], m: int) -> int:
3        answer=0
4        n=len(position)
5        position.sort()
6        def can_place_balls(x,position,m):
7            prev_balls_pos=position[0]
8            balls_placed=1
9
10            for i in range(1,len(position)):
11                curr_pos=position[i]
12                if curr_pos-prev_balls_pos>=x:
13                    balls_placed+=1
14                    prev_balls_pos=curr_pos
15                if balls_placed==m:
16                    return True
17            return False
18
19
20        #initial search space
21        low=1
22        high = (position[-1] - position[0]) // (m - 1)
23
24        while low<=high:
25            mid=low+(high-low)//2
26            if can_place_balls(mid,position,m):
27                answer=mid
28                low=mid+1   #discard the left half search space as it is not valid
29            else:
30                high=mid-1  #discard the right half search space as it is not valid
31        return answer