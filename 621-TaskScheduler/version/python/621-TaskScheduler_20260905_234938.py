# Last updated: 9/5/2026, 11:49:38 PM
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
18
19        # count=Counter(tasks)
20        # maxheap=[-cnt for cnt in count.values()]
21        # time=0
22        # q=deque()
23        # heapq.heapify(maxheap)
24
25        # while maxheap or q:
26        #     time+=1
27        #     if maxheap:
28        #         cnt=1+heapq.heappop(maxheap)
29        #         if cnt:
30        #             q.append([cnt,time+n])
31        #     if q and q[0][1]==time:
32        #         heapq.heappush(maxheap,q.popleft()[0])
33        # return time