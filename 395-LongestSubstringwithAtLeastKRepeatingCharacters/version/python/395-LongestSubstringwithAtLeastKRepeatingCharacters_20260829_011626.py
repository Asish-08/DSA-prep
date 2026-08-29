# Last updated: 8/29/2026, 1:16:26 AM
1class Solution:
2    def longestSubstring(self, s: str, k: int) -> int:
3
4        if len(s) < k:
5            return 0
6
7        count = Counter(s)
8
9        for char in count:
10
11            if count[char] < k:
12
13                # Split at the first occurrence of the invalid character.
14                left, right = s.split(char, 1)
15
16                # Solve the two substrings recursively.
17                left = self.longestSubstring(left, k)
18                right = self.longestSubstring(right, k)
19
20                return max(left, right)
21
22        return len(s)