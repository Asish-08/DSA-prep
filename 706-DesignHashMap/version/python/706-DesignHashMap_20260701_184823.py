# Last updated: 7/1/2026, 6:48:23 PM
1class ListNode:
2    def __init__(self,key=-1,val=-1,next=None):
3        self.key=key
4        self.val=val
5        self.next=next
6
7class MyHashMap:
8
9    def __init__(self):
10        self.h_map=[ListNode() for i in range(10**6)]
11
12    def hash(self,key):
13        return key%len(self.h_map)
14
15    def put(self, key: int, value: int) -> None:
16        cur=self.h_map[self.hash(key)]
17        while cur.next:
18            if cur.next.key==key:
19                cur.next.val=value
20                return
21            cur=cur.next
22        cur.next= ListNode(key,value)
23
24    def get(self, key: int) -> int:
25        cur=self.h_map[self.hash(key)]
26        while cur.next:
27            if cur.next.key==key:
28                return cur.next.val
29            cur=cur.next
30        return -1
31        
32    def remove(self, key: int) -> None:
33        cur=self.h_map[self.hash(key)]
34        while cur.next:
35            if cur.next.key==key:
36                cur.next=cur.next.next
37                return
38            cur=cur.next
39        
40
41
42# Your MyHashMap object will be instantiated and called as such:
43# obj = MyHashMap()
44# obj.put(key,value)
45# param_2 = obj.get(key)
46# obj.remove(key)