# Last updated: 9/26/2026, 7:41:10 AM
1class Solution:
2    def findCircleNum(self, isConnected: List[List[int]]) -> int:
3        visited=set()
4        provinces=0
5
6        def dfs(city):
7            for nei in range(len(isConnected)):
8                if nei not in visited and isConnected[city][nei]==1:
9                    visited.add(nei)
10                    dfs(nei)
11                    
12
13            
14
15
16        for city in range(len(isConnected)):
17            if city not in visited:
18                dfs(city)
19                provinces+=1
20        return provinces
21            
22
23
24
25
26
27
28        # def dfs(city):
29        #     for neighbor in range(len(isConnected)):
30        #         if neighbor not in visited and isConnected[city][neighbor]==1:
31        #             visited.add(neighbor)
32        #             dfs(neighbor)
33        # visited=set()
34        # provinces=0
35        # for city in range(len(isConnected)):
36        #     if city not in visited:
37        #         dfs(city)
38        #         provinces+=1
39        # return provinces
40
41