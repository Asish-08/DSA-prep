# Last updated: 3/28/2026, 1:22:54 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        i,j=0,len(s)-1
4        while i<j:
5            while i<j and not s[i].isalnum():
6                i+=1
7            while i<j and not s[j].isalnum():
8                j-=1
9            if i<j and s[i].lower()!= s[j].lower():
10                return False
11            i+=1
12            j-=1
13        return True