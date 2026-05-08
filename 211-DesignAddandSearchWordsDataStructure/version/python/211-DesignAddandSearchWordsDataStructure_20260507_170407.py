# Last updated: 5/7/2026, 5:04:07 PM
1class TrieNode:
2    def __init__(self):
3        self.children={}
4        self.endofWord=False
5
6class WordDictionary:
7
8    def __init__(self):
9        self.root=TrieNode()
10        
11
12    def addWord(self, word: str) -> None:
13        curr=self.root
14
15        for c in word:
16            if c not in curr.children:
17                curr.children[c]=TrieNode()
18            curr=curr.children[c]
19        curr.endofWord=True
20        
21
22    def search(self, word: str) -> bool:
23        def dfs(index, node):
24            curr=node
25
26            for i in range(index, len(word)):
27                c=word[i]
28
29                if c=='.':
30                    for child in curr.children.values():
31                        if dfs(i+1,child):
32                            return True
33                    return False
34                
35                if c not in curr.children:
36                    return False
37                
38                curr=curr.children[c]
39            return curr.endofWord
40        return dfs(0,self.root)
41# Your WordDictionary object will be instantiated and called as such:
42# obj = WordDictionary()
43# obj.addWord(word)
44# param_2 = obj.search(word)