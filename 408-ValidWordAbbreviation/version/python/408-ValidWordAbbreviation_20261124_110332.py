# Last updated: 11/24/2026, 11:03:32 AM
1class Solution:
2    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
3        #Two pointer Approach
4        i,j=0,0
5
6        while j<len(abbr):
7            if abbr[j].isalpha():
8                if i>=len(word) or word[i]!=abbr[j]:
9                    return False
10                i+=1
11                j+=1
12            else:
13                if abbr[j]=='0':
14                    return False
15                num=0
16
17                while j<len(abbr) and abbr[j].isdigit():
18                    num=num*10+int(abbr[j])
19                    j+=1
20                i+=num
21
22                if i>len(word):
23                    return False
24        return i==len(word)
25
26        