# Last updated: 5/7/2026, 4:19:34 PM
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
12        curr=self.root
13
14        for c in word:
15            if c not in curr.children:
16                curr.children[c]=TrieNode()
17            curr=curr.children[c]
18        curr.endofWord=True
19
20    def search(self, word: str) -> bool:
21        curr=self.root
22
23        for c in word:
24            if c not in curr.children:
25                return False
26            curr=curr.children[c]
27        return curr.endofWord
28        
29
30    def startsWith(self, prefix: str) -> bool:
31        curr=self.root
32
33        for c in prefix:
34            if c not in curr.children:
35                return False
36            curr=curr.children[c]
37        return True
38        
39
40
41# Your Trie object will be instantiated and called as such:
42# obj = Trie()
43# obj.insert(word)
44# param_2 = obj.search(word)
45# param_3 = obj.startsWith(prefix)