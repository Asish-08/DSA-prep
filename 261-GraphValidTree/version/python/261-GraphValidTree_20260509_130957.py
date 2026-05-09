# Last updated: 5/9/2026, 1:09:57 PM
1class Solution:
2    def validTree(self, n: int, edges: List[List[int]]) -> bool:
3        if len(edges)!=n-1:
4            return False
5        
6        visited=set()
7        graph={i:[] for i in range(n)}
8
9        for a,b in edges:
10            graph[a].append(b)
11            graph[b].append(a)
12
13        def dfs(node):
14            if node in visited:
15                return 
16            visited.add(node)
17            for nei in graph[node]:
18                dfs(nei)
19            
20        
21        dfs(0)
22        return len(visited)==n