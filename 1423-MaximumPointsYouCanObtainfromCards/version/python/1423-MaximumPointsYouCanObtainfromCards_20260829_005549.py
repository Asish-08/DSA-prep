# Last updated: 8/29/2026, 12:55:49 AM
1class Solution:
2    def maxScore(self, cardPoints: List[int], k: int) -> int:
3        left=0
4        right=len(cardPoints)-k
5        total=sum(cardPoints[right:])
6        res=total
7
8        while right<len(cardPoints):
9            total=total+cardPoints[left]-cardPoints[right]
10            left+=1
11            right+=1
12            res=max(res,total)
13        return res