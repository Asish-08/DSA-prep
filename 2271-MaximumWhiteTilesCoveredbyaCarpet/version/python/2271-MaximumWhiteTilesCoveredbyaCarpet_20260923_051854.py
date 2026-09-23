# Last updated: 9/23/2026, 5:18:54 AM
1class Solution:
2    def maximumWhiteTiles(self, tiles: list[list[int]], carpetLen: int) -> int:
3        tiles.sort(key=lambda x: x[0])
4        l=0
5        max_covered=0
6        covered=0
7
8        for r in range(len(tiles)):
9            start,end=tiles[r]
10            covered+=end-start+1
11
12            while tiles[r][1]-tiles[l][0]+1>carpetLen:
13                covered-=tiles[l][1]-tiles[l][0]+1
14                l+=1
15
16                if l>r:
17                    break
18            max_covered=max(max_covered,covered)
19            if l>0:
20                carpet_start=tiles[r][1]-carpetLen+1
21                partial=max(0,tiles[l-1][1]-carpet_start+1)
22                max_covered=max(max_covered,covered+partial)
23            if max_covered>=carpetLen:
24                return carpetLen
25        return max_covered
26