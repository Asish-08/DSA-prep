# Last updated: 5/6/2026, 12:26:00 PM
1class Node:
2    def __init__(self,key,val):
3        self.key, self.val=key,val
4        self.prev,self.nex=None,None
5
6class LRUCache:
7
8    def __init__(self, capacity: int):
9        self.cap=capacity
10        self.cache={} #map key to node
11
12        #LRU left side and most recent on the right
13        self.left,self.right=Node(0,0),Node(0,0)
14        # correct dummy connections
15        self.left.next = self.right
16        self.right.prev = self.left
17    
18    def remove(self,node):
19        # remove node from the list
20        prev,nxt=node.prev,node.next
21        prev.next, nxt.prev= nxt,prev
22    def insert(self,node):
23        # insert node to the right to the list
24        prev,nxt=self.right.prev, self.right
25        prev.next=nxt.prev= node
26        node.next, node.prev=nxt,prev
27
28
29
30    def get(self, key: int) -> int:
31        if key in self.cache:
32            self.remove(self.cache[key])
33            self.insert(self.cache[key])
34
35            return self.cache[key].val
36        return -1
37        
38
39    def put(self, key: int, value: int) -> None:
40        if key in self.cache:
41            self.remove(self.cache[key])
42        self.cache[key]=Node(key,value)
43        self.insert(self.cache[key])
44        if len(self.cache)>self.cap:
45            lru=self.left.next
46            self.remove(lru)
47            del self.cache[lru.key]
48        
49
50
51# Your LRUCache object will be instantiated and called as such:
52# obj = LRUCache(capacity)
53# param_1 = obj.get(key)
54# obj.put(key,value)