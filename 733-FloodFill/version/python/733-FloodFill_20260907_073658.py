# Last updated: 9/7/2026, 7:36:58 AM
1class Solution:
2    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
3        R,C=len(image),len(image[0])
4        curr=image[sr][sc]
5        if curr==color:
6            return image
7        def dfs(r,c):
8            if image[r][c]==curr:
9                image[r][c]=color
10
11                if r+1<R:
12                    dfs(r+1,c)
13                if r-1>=0:
14                    dfs(r-1,c)
15                if c-1>=0:
16                    dfs(r,c-1)
17                if c+1<C:
18                    dfs(r,c+1)
19        dfs(sr,sc)
20        return image
21
22
23
24        
25        # R,C= len(image),len(image[0])
26        
27        # curr=image[sr][sc]
28        
29        # if curr==color:
30        #     return image
31        
32        # def dfs(r,c):
33        #     if image[r][c]==curr:
34        #         image[r][c]=color
35            
36        #         if r>=1:
37        #             dfs(r-1,c)
38        #         if r+1< R:
39        #             dfs(r+1,c)
40        #         if c>=1:
41        #             dfs(r,c-1)
42        #         if c+1 <C:
43        #             dfs(r,c+1)
44        # dfs(sr,sc)
45        # return image