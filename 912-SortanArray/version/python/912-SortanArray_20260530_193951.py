# Last updated: 5/30/2026, 7:39:51 PM
1class Solution:
2    def sortArray(self, nums: List[int]) -> List[int]:
3        self.mergesort(nums,0,len(nums)-1)
4        return nums
5
6    def mergesort(self, nums: List[int], left: int, right: int) -> None:
7        if left>=right:
8            return
9        mid=(left+right)//2
10        self.mergesort(nums,left,mid)
11        self.mergesort(nums,mid+1,right)
12
13        self.merge(nums, left, mid, right)
14    
15    def merge(self, nums: List[int], left: int, mid: int, right: int) -> None:
16        left_half= nums[left:mid+1]
17        right_half= nums[mid+1:right+1]
18
19        i,j=0,0
20        k=left
21
22        while i<len(left_half) and j<len(right_half):
23            if left_half[i]<=right_half[j]:
24                nums[k]=left_half[i]
25                i+=1
26            else:
27                nums[k]=right_half[j]
28                j+=1
29            k+=1
30
31        while i <len(left_half):
32            nums[k]=left_half[i]
33            i+=1
34            k+=1
35        
36        while j<len(right_half):
37            nums[k]=right_half[j]
38            j+=1
39            k+=1
40            
41        
42
43
44