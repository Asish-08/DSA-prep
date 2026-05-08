# Last updated: 5/7/2026, 9:16:01 PM
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        res=[]
4        def backtracking(remain,comb,start):
5            if remain==0:
6                res.append(list(comb))
7                return
8            elif remain<0:
9                return
10            
11            for i in range(start,len(candidates)):
12                comb.append(candidates[i])
13                backtracking(remain-candidates[i],comb,i)
14                comb.pop()
15        backtracking(target,[],0)
16        return res