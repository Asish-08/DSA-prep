# Last updated: 9/25/2026, 6:35:57 PM
1class Solution:
2    def maxDistance(self, position: list[int], m: int) -> int:
3        answer=0
4        position.sort()
5        n=len(position)
6        
7        def can_place_balls(x,position,m):
8            prev_balls_pos=position[0]
9            balls_placed=1
10            for i in range(len(position)):
11                curr_pos=position[i]
12                if curr_pos-prev_balls_pos>=x:
13                    prev_balls_pos=position[i]
14                    balls_placed+=1
15                if balls_placed==m:
16                    return True
17            return False
18
19
20        #initial search space
21        low=1
22        high=(position[-1]-position[0])//(m-1)
23
24        while low<=high:
25            mid=low+(high-low)//2
26            if can_place_balls(mid,position,m):
27                answer=mid
28                low=mid+1
29            else:
30                high=mid-1
31        return answer
32
33
34
35
36
37
38
39
40
41
42
43        # answer=0
44        # n=len(position)
45        # position.sort()
46        # def can_place_balls(x,position,m):
47        #     prev_balls_pos=position[0]
48        #     balls_placed=1
49
50        #     for i in range(1,len(position)):
51        #         curr_pos=position[i]
52        #         if curr_pos-prev_balls_pos>=x:
53        #             balls_placed+=1
54        #             prev_balls_pos=curr_pos
55        #         if balls_placed==m:
56        #             return True
57        #     return False
58
59
60        # #initial search space
61        # low=1
62        # high = (position[-1] - position[0]) // (m - 1)
63
64        # while low<=high:
65        #     mid=low+(high-low)//2
66        #     if can_place_balls(mid,position,m):
67        #         answer=mid
68        #         low=mid+1   #discard the left half search space as it is not valid
69        #     else:
70        #         high=mid-1  #discard the right half search space as it is not valid
71        # return answer