# Last updated: 4/30/2026, 1:53:46 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        n=len(s)
        freq={}
        max_freq=0
        res=0
        for right in range(n):
            freq[s[right]]=freq.get(s[right],0)+1
            max_freq = max(max_freq, freq[s[right]])

            l=right-left+1
            if l-max_freq>k:
                freq[s[left]]-=1
                left+=1
            res=max(res,right-left+1)
        return res
            


            
        