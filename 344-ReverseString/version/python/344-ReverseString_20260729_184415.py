# Last updated: 7/29/2026, 6:44:15 PM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) <= 1:
            return s
        l ,r = 0, len(s) -1
        while l < r:
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp
            l += 1
            r -= 1
        return s