# Last updated: 8/28/2026, 4:41:54 PM
1class Solution:
2    def totalFruit(self, fruits: List[int]) -> int:
3        count=Counter()
4        left=0
5        result=0
6
7        for right in range(len(fruits)):
8            count[fruits[right]]+=1
9
10            if len(count)>2:
11                count[fruits[left]]-=1
12
13                if count[fruits[left]]==0:
14                    del count[fruits[left]]
15                left+=1
16            result=max(result,right-left+1)
17        return result