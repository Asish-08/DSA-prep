# Last updated: 7/12/2026, 1:03:07 PM
1class Solution:
2    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
3        N=len(grid)
4
5        def in_bound(r,c):
6            return min(r,c)>=0 and max(r,c)< N
7
8        def precompute():
9            q=deque()
10            min_dist={}
11            for r in range(N):
12                for c in range(N):
13                    if grid[r][c]:
14                        q.append([r,c,0])
15                        min_dist[(r,c)]=0
16            while q:
17                r,c,dist=q.popleft()
18                nei=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
19                for r2,c2 in nei:
20                    if in_bound(r2,c2) and (r2,c2) not in min_dist:
21                        min_dist[(r2,c2)]=dist+1
22                        q.append([r2,c2,dist+1])
23            return min_dist
24        
25        min_dist=precompute()
26        max_heap=[(-min_dist[(0,0)],0,0)] #(dist,r,c)
27        visit=set()
28        visit.add((0,0))
29        while max_heap:
30            dist,r,c=heapq.heappop(max_heap)
31            dist=-dist
32            if (r,c) ==(N-1,N-1):
33                return dist
34            nei=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
35            for r2,c2 in nei:
36                if in_bound(r2,c2) and (r2,c2) not in visit:
37                    visit.add((r2,c2))
38                    dist2= min(dist,min_dist[(r2,c2)])
39                    heapq.heappush(max_heap,(-dist2,r2,c2))
40            
41
42