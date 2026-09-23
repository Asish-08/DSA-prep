# Last updated: 9/22/2026, 8:35:44 PM
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
18
19        romandigits=[]
20
21        for val,sym in digits:
22            q,r=divmod(num,val)
23            romandigits.append(q*sym)
24            num=r
25
26        return ''.join(romandigits)
27
28                
29                
30        