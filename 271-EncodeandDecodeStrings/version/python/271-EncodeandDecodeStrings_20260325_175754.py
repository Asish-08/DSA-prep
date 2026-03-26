# Last updated: 3/25/2026, 5:57:54 PM
1class Codec:
2    def encode(self, strs: List[str]) -> str:
3        """Encodes a list of strings to a single string.
4        """
5        return 'π'.join(strs)
6        
7
8    def decode(self, s: str) -> List[str]:
9        """Decodes a single string to a list of strings.
10        """
11        return s.split('π')
12        
13
14
15# Your Codec object will be instantiated and called as such:
16# codec = Codec()
17# codec.decode(codec.encode(strs))