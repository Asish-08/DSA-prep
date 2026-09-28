# Last updated: 9/27/2026, 5:35:42 PM
1class Solution:
2    def compress(self, chars: List[str]) -> int:
3        i=0
4        write=0
5        while i<len(chars):
6            char=chars[i]
7            count=0
8            while  i<len(chars) and chars[i]==char:
9                i+=1
10                count+=1
11            chars[write]=char
12            write+=1
13
14            if count>1:
15                for digit in str(count):
16                    chars[write]=digit
17                    write+=1
18        return write
19
20        # i=0
21        # write=0
22        # while i<len(chars):
23        #     char=chars[i]
24        #     count=0
25
26        #     while i<len(chars) and chars[i]==char:
27        #         count+=1
28        #         i+=1
29        #     chars[write]=char
30        #     write+=1
31
32        #     if count>1:
33        #         for digit in str(count):
34        #             chars[write]=digit
35        #             write+=1
36        # return write
37
38            
39
40        