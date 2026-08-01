# Last updated: 7/31/2026, 8:11:49 PM
1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        # boat=0
4        # l,r=0,1
5        # while r<len(people):
6        #     if people[l]+people[r]==limit:
7        #         boat+=1
8        #     elif people[l]+people[r]>limit:
9        #         boat+=math.ceil(limit/2)
10        #     l+=1
11        #     r+=1
12        #     return boat
13        boat=0
14        people.sort()
15        l,r=0,len(people)-1
16        while l<=r:
17            if people[l]+people[r]<=limit:
18                l+=1
19                r-=1
20            else:
21                r-=1
22            boat+=1
23        return boat
24