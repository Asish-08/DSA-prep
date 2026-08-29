# Last updated: 8/28/2026, 10:15:11 PM
1class Solution:
2    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
3        count={}
4        left=0
5        max_sum=0
6        curr_sum=0
7        
8        for right in range(len(nums)):
9            count[nums[right]]=count.get(nums[right],0)+1
10            curr_sum+=nums[right]
11             # Keep the window size exactly k.
12            if right-left+1>k:
13                curr_sum-=nums[left]
14                count[nums[left]]-=1
15
16                if count[nums[left]]==0:
17                    del count[nums[left]]
18                left+=1
19            # If the window has k distinct elements, update the answer.
20            if right-left+1==k and len(count)==k:
21                max_sum=max(max_sum,curr_sum)
22        return max_sum
23
24
25
26
27
28        # curr_sum=sum(nums[:k])
29        # max_sum=0
30
31        # seen=set(nums[:k])
32        # if len(seen)==k:
33        #     max_sum=curr_sum
34        
35        # left=0
36        # for right in range(k, len(nums)):
37        #     #adding the new element in the window
38        #     curr_sum+=nums[right]
39        #     #subtracting the left element from the window after considering new element
40        #     curr_sum-=nums[left]
41        #     left+=1
42        #     #updating the window
43        #     window=nums[left:right+1]
44
45        #     #checking for any duplicates
46        #     if len(set(window))==k:
47        #         max_sum=max(max_sum,curr_sum)
48        # return max_sum
49
50
51