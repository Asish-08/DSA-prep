# Last updated: 5/9/2026, 11:46:26 AM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        preMap={i:[] for i in range(numCourses)}
4        for crs,pre in prerequisites:
5            preMap[crs].append(pre)
6        
7        visitSet=set()
8        def dfs(crs):
9            if crs in visitSet:
10                return False
11            if preMap[crs]==[]:
12                return True
13            visitSet.add(crs)
14            for pre in preMap[crs]:
15                if not dfs(pre): return False
16            visitSet.remove(crs)
17            preMap[crs]=[]
18            return True
19
20
21
22        for crs in range(numCourses):
23            if not dfs(crs): return False
24        return True
25