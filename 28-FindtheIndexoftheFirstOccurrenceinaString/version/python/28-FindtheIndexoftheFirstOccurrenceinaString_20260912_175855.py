# Last updated: 9/12/2026, 5:58:55 PM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle not in haystack:
        #     return -1

        # if needle in haystack:
        #     return(haystack.find(needle))

        l_stack = len(haystack)
        l_needle = len(needle)
        to_loop = l_stack-l_needle +1 

        for i in range(to_loop):
            if haystack[i:i+l_needle] == needle:
                return i
        return -1
