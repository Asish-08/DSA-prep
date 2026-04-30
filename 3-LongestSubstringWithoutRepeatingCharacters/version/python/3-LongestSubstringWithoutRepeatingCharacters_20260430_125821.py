# Last updated: 4/30/2026, 12:58:21 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        i = 0
        length = 0
        for j in range(len(s)):
            while s[j] in char:
                char.remove(s[i])
                i += 1
            char.add(s[j])
            if len(char) > length:
                length = len(char)
        return length
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))        