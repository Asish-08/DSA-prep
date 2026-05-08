# Last updated: 5/8/2026, 12:04:37 AM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        res=[]
4        digittochar={
5            '2':"abc",
6            '3':"def",
7            '4':"ghi",
8            '5':"jkl",
9            '6':"mno",
10            '7':"pqrs",
11            '8':"tuv",
12            '9':"wxyz"
13        }
14        def backtrack(i,currstr):
15            if i==len(digits):
16                res.append(currstr[:])
17                return
18            for n in digittochar[digits[i]]:
19                backtrack(i+1,currstr+n)
20        backtrack(0,"")
21        return res
22