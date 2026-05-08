# Last updated: 5/8/2026, 2:09:20 PM
1class Solution:
2    def leastInterval(self, tasks: List[str], n: int) -> int:
3        count=Counter(tasks)
4        maxHeap=[-cnt for cnt in count.values()]
5        q=deque()
6        time=0
7        heapq.heapify(maxHeap)
8
9        while maxHeap or q:
10            time+=1
11            if maxHeap:
12                cnt=1+heapq.heappop(maxHeap)
13                if cnt:
14                    q.append([cnt,time+n])
15            if q and q[0][1]==time:
16                heapq.heappush(maxHeap,q.popleft()[0])
17        return time