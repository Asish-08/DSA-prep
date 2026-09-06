# Last updated: 9/5/2026, 10:03:29 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        # using heap
4        count=Counter(nums)
5        heap=[]
6        res=[]
7
8        for key,val in count.items():
9            heapq.heappush(heap,(-val,key))
10        heapq.heapify(heap)
11
12        for _ in range(k):
13            val,key=heapq.heappop(heap)
14            res.append(key)
15        return res
16
17        
18        # using bucketsort to sort the K freqent elements
19        # hashmap=Counter(nums)
20
21        # buckets=[[] for _ in range(len(nums)+1)]
22
23        # for num,freq in hashmap.items():
24        #     buckets[freq].append(num)
25        
26        # res=[]
27        # for freq in range(len(buckets)-1,0,-1):
28        #     for num in buckets[freq]:
29        #         res.append(num)
30        #         if len(res)==k:
31        #             return res
32
33