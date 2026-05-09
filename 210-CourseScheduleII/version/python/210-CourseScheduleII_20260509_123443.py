# Last updated: 5/9/2026, 12:34:43 PM
1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
3        preMap={i:[] for i in range(numCourses)}
4
5        for crs,pre in prerequisites:
6            preMap[crs].append(pre)
7        
8        visitSet=set()
9        visited=set()
10        res=[]
11
12        def dfs(crs):
13            if crs in visitSet:
14                return False
15            if crs in visited:
16                return True
17            visitSet.add(crs)
18
19            for pre in preMap[crs]:
20                if not dfs(pre):
21                    return False
22            visitSet.remove(crs)
23            visited.add(crs)
24            res.append(crs)
25
26            return True
27
28
29
30        for crs in range(numCourses):
31            if not dfs(crs): return []
32        return res