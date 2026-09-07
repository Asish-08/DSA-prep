# Last updated: 9/7/2026, 8:08:46 AM
1class Solution:
2    def findCircleNum(self, isConnected: List[List[int]]) -> int:
3        # def dfs(city):
4        #     for neighbor in range(len(isConnected)):
5        #         if isConnected[city][neighbor]==1 and neighbor not in visited:
6        #             visited.add(neighbor)
7        #             dfs(neighbor)
8        
9        # visited=set()
10        # provinces=0
11        # for city in range(len(isConnected)):
12        #     if city  not in visited:
13        #         dfs(city)
14        #         provinces+=1
15        # return provinces
16
17        def dfs(city):
18            for neighbor in range(len(isConnected)):
19                if neighbor not in visited and isConnected[city][neighbor]==1:
20                    visited.add(neighbor)
21                    dfs(neighbor)
22        visited=set()
23        provinces=0
24        for city in range(len(isConnected)):
25            if city not in visited:
26                dfs(city)
27                provinces+=1
28        return provinces
29
30