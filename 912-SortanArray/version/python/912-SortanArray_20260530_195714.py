# Last updated: 5/30/2026, 7:57:14 PM
1class Solution:
2    def sortArray(self, nums: List[int]) -> List[int]:
3        if len(nums)<=1:
4            return nums
5        mid=len(nums)//2
6        left_half=self.sortArray(nums[:mid])
7        right_half=self.sortArray(nums[mid:])
8
9        return self.merge_sort(left_half,right_half)
10    
11    def merge_sort(self, left:list[int], right:list[int])-> list[int]:
12        sorted_arr=[]
13        i,j=0,0
14
15        #comparing and adding the elements into sorted_arr 
16        while i<len(left) and j<len(right):
17            if left[i]<right[j]:
18                sorted_arr.append(left[i])
19                i+=1
20            else:
21                sorted_arr.append(right[j])
22                j+=1
23        
24        #adding the rem elements in left and right
25        sorted_arr.extend(left[i:])
26        sorted_arr.extend(right[j:])
27
28        return sorted_arr
29