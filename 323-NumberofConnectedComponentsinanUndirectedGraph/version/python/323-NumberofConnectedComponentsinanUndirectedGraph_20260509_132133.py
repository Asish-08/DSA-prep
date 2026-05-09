# Last updated: 5/9/2026, 1:21:33 PM
1class Solution:
2    def countComponents(self, n: int, edges: List[List[int]]) -> int:
3        visited=set()
4        graph={i:[] for i in range(n)}
5        count=0
6
7        for a,b in edges:
8            graph[a].append(b)
9            graph[b].append(a)
10        
11        def dfs(node):
12            if node in visited:
13                return
14            visited.add(node)
15            for nei in graph[node]:
16                dfs(nei)
17            
18        
19        for node in range(n):
20            if node not in visited:
21                count+=1
22                dfs(node)
23        return count
24