# Last updated: 5/8/2026, 2:13:07 PM
1class Solution:
2    def leastInterval(self, tasks: List[str], n: int) -> int:
3        count=Counter(tasks)
4        maxheap=[-cnt for cnt in count.values()]
5        time=0
6        q=deque()
7        heapq.heapify(maxheap)
8
9        while maxheap or q:
10            time+=1
11            if maxheap:
12                cnt=1+heapq.heappop(maxheap)
13                if cnt:
14                    q.append([cnt,time+n])
15            if q and q[0][1]==time:
16                heapq.heappush(maxheap,q.popleft()[0])
17        return time