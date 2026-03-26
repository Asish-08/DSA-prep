# Last updated: 3/25/2026, 5:32:44 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        # using heap
4        # count=Counter(nums)
5        # heap=[]
6        # res=[]
7        # for num,freq in count.items():
8        #     heap.append((-freq,num))
9        # heapq.heapify(heap)
10
11        # for _ in range(k):
12        #     freq,num=heapq.heappop(heap)
13        #     res.append(num)
14        # return res
15
16        # using bucketsort
17        hashmap=Counter(nums)
18
19        buckets=[[] for _ in range(len(nums)+1)]
20
21        for num,freq in hashmap.items():
22            buckets[freq].append(num)
23        
24        res=[]
25        for freq in range(len(buckets)-1,0,-1):
26            for num in buckets[freq]:
27                res.append(num)
28                if len(res)==k:
29                    return res
30
31