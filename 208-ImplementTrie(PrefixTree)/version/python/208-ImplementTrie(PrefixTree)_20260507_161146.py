# Last updated: 5/7/2026, 4:11:46 PM
1class TrieNode:
2    def __init__(self):
3        self.children={}
4        self.endofWord=False
5
6class Trie:
7
8    def __init__(self):
9        self.root=TrieNode()
10
11    def insert(self, word: str) -> None:
12        cur=self.root
13
14        for c in word:
15            if c not in cur.children:
16                cur.children[c]=TrieNode()
17            cur=cur.children[c]
18        cur.endofWord=True
19
20    def search(self, word: str) -> bool:
21        cur=self.root
22
23        for c in word:
24            if c not in cur.children:
25                return False
26            cur=cur.children[c]
27        return cur.endofWord
28        
29
30    def startsWith(self, prefix: str) -> bool:
31        cur=self.root
32
33        for c in prefix:
34            if c not in cur.children:
35                return False
36            cur=cur.children[c]
37        return True
38
39
40# Your Trie object will be instantiated and called as such:
41# obj = Trie()
42# obj.insert(word)
43# param_2 = obj.search(word)
44# param_3 = obj.startsWith(prefix)