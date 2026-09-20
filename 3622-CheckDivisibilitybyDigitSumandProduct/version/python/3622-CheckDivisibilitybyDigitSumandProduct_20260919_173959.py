# Last updated: 9/19/2026, 5:39:59 PM
1class Solution:
2    def checkDivisibility(self, n: int) -> bool:
3        sum_of_digits=0
4        prod_of_digits=1
5        copy_n=n
6        while n:
7            n,r=divmod(n,10)
8            sum_of_digits+=r
9            prod_of_digits*=r
10        if copy_n != 0:
11            check=copy_n % (sum_of_digits+prod_of_digits)
12        if check==0:
13            return True
14        
15        return False
16
17
18        