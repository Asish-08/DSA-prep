# Last updated: 9/27/2026, 3:45:22 PM
1class Solution:
2    def intToRoman(self, num: int) -> str:
3        digits = [
4            (1000, "M"),
5            (900, "CM"),
6            (500, "D"),
7            (400, "CD"),            #*******
8            (100, "C"),             #reveiew again
9            (90, "XC"),
10            (50, "L"),
11            (40, "XL"),
12            (10, "X"),
13            (9, "IX"),
14            (5, "V"),
15            (4, "IV"),
16            (1, "I"),
17        ]
18        romandigits=[]
19        for val,sym in digits:
20            if num==0:
21                break
22            q,r=divmod(num,val)
23            num=r
24            romandigits.append(q*sym)
25        return ''.join(romandigits)
26        
27                
28                
29        