# Last updated: 9/22/2026, 8:20:02 PM
1class Solution:
2    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
3        R,C=len(image),len(image[0])
4        curr=image[sr][sc]
5        if curr==color:
6            return image
7        
8        def dfs(r,c):
9            if image[r][c]==curr:
10                image[r][c]=color
11                if r+1<R:
12                    dfs(r+1,c)
13                if r-1>=0:
14                    dfs(r-1,c)
15                if c+1<C:
16                    dfs(r,c+1)
17                if c-1>=0:
18                    dfs(r,c-1)
19        dfs(sr,sc)
20        return image
21
22
23
24
25
26
27
28
29
30        # R,C=len(image),len(image[0])
31        # curr=image[sr][sc]
32        # if curr==color:
33        #     return image
34        # def dfs(r,c):
35        #     if image[r][c]==curr:
36        #         image[r][c]=color
37
38        #         if r+1<R:
39        #             dfs(r+1,c)
40        #         if r-1>=0:
41        #             dfs(r-1,c)
42        #         if c-1>=0:
43        #             dfs(r,c-1)
44        #         if c+1<C:
45        #             dfs(r,c+1)
46        # dfs(sr,sc)
47        # return image
48
49
50
51        
52        # R,C= len(image),len(image[0])
53        
54        # curr=image[sr][sc]
55        
56        # if curr==color:
57        #     return image
58        
59        # def dfs(r,c):
60        #     if image[r][c]==curr:
61        #         image[r][c]=color
62            
63        #         if r>=1:
64        #             dfs(r-1,c)
65        #         if r+1< R:
66        #             dfs(r+1,c)
67        #         if c>=1:
68        #             dfs(r,c-1)
69        #         if c+1 <C:
70        #             dfs(r,c+1)
71        # dfs(sr,sc)
72        # return image