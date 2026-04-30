# Last updated: 4/29/2026, 6:51:47 PM
1class TimeMap:
2
3    def __init__(self):
4        self.store={} #hashamp key,value initialization
5
6    def set(self, key: str, value: str, timestamp: int) -> None:
7        if key not in self.store:
8            self.store[key]=[]
9        self.store[key].append([value,timestamp])
10
11    def get(self, key: str, timestamp: int) -> str:
12        res=''
13        values=self.store.get(key,[])
14        
15        l,r=0,len(values)-1
16        while l<=r:
17            m=(l+r)//2
18            if values[m][1]<=timestamp:
19                res=values[m][0]
20                l=m+1
21            else:
22                r=m-1
23        return res
24    
25
26
27# Your TimeMap object will be instantiated and called as such:
28# obj = TimeMap()
29# obj.set(key,value,timestamp)
30# param_2 = obj.get(key,timestamp)