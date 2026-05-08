# Last updated: 5/7/2026, 9:51:25 PM
1class Solution:
2    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
3        res=[]
4        candidates.sort()
5        def backtrack(remain,comb,start):
6            if remain==0:
7                res.append(comb.copy())
8                return
9            elif remain<0:
10                return
11            
12            for i in range(start,len(candidates)):
13                if i>start and candidates[i]==candidates[i-1]:
14                    continue
15                comb.append(candidates[i])
16                backtrack(remain-candidates[i],comb,i+1)
17                comb.pop()
18        backtrack(target,[],0)
19        return res