# Last updated: 7/1/2026, 6:34:53 PM
1class ListNode:
2    def __init__(self,key):
3        self.key=key
4        self.next=None
5class MyHashSet:
6
7    def __init__(self):
8        self.set=[ListNode(0) for i in range(10**4)]
9
10    def add(self, key: int) -> None:
11        cur=self.set[key%len(self.set)]
12        while cur.next:
13            if cur.next.key==key:
14                return
15            cur=cur.next
16        cur.next=ListNode(key)
17
18    def remove(self, key: int) -> None:
19        cur=self.set[key%len(self.set)]
20        while cur.next:
21            if cur.next.key==key:
22                cur.next=cur.next.next
23                return
24            cur=cur.next
25
26    def contains(self, key: int) -> bool:
27        cur=self.set[key%len(self.set)]
28        while cur.next:
29            if cur.next.key==key:
30                return True
31            cur=cur.next
32        return False
33        
34
35
36# Your MyHashSet object will be instantiated and called as such:
37# obj = MyHashSet()
38# obj.add(key)
39# obj.remove(key)
40# param_3 = obj.contains(key)