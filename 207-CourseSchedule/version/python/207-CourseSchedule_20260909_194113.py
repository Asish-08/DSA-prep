# Last updated: 9/9/2026, 7:41:13 PM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        premap={i:[] for i in range(numCourses)}
4        for crs,pre in prerequisites:
5            premap[crs].append(pre)
6        
7        visit_set=set()
8        def dfs(crs):
9            if crs in visit_set:
10                return False
11            if premap[crs]==[]:
12                return True
13            visit_set.add(crs)
14            for pre in premap[crs]:
15                if not dfs(pre): return False
16            visit_set.remove(crs)
17            premap[crs]=[]
18            return True  
19        
20        for crs in range(numCourses):
21            if not dfs(crs):
22                return False
23        return True
24
25        # preMap={i:[] for i in range(numCourses)}
26        # for crs,pre in prerequisites:
27        #     preMap[crs].append(pre)
28        
29        # visitSet=set()
30        # def dfs(crs):
31        #     if crs in visitSet:
32        #         return False
33        #     if preMap[crs]==[]:
34        #         return True
35        #     visitSet.add(crs)
36        #     for pre in preMap[crs]:
37        #         if not dfs(pre): return False
38        #     visitSet.remove(crs)
39        #     preMap[crs]=[]
40        #     return True
41
42
43
44        for crs in range(numCourses):
45            if not dfs(crs): return False
46        return True
47