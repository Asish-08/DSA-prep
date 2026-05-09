# Last updated: 5/8/2026, 10:07:02 PM
1class Solution:
2    def wallsAndGates(self, rooms: List[List[int]]) -> None:
3        """
4        Do not return anything, modify rooms in-place instead.
5        """
6        Rows,Cols=len(rooms),len(rooms[0])
7        visit=set()
8        q=deque()
9        
10        def addrooms(r,c):
11            if (r<0 or c<0 or r==Rows or c==Cols or (r,c) in visit or rooms[r][c]==-1):
12                return
13            q.append([r,c])
14            visit.add((r,c))
15
16        for r in range(Rows):
17            for c in range(Cols):
18                if rooms[r][c]==0:
19                    q.append([r,c])
20                    visit.add((r,c))
21        dist=0
22        while q:
23            for i in range(len(q)):
24                r,c=q.popleft()
25                rooms[r][c]=dist
26                
27                addrooms(r+1,c)
28                addrooms(r-1,c)
29                addrooms(r,c+1)
30                addrooms(r,c-1)
31            dist+=1
32        
33        