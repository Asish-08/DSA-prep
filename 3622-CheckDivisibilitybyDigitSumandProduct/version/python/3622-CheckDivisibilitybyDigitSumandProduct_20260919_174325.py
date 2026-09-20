# Last updated: 9/19/2026, 5:43:25 PM
1class Solution:
2    def checkDivisibility(self, n: int) -> bool:
3        sum_of_digits=0
4        prod_of_digits=1
5        copy_n=n
6        while copy_n:
7            copy_n,r=divmod(copy_n,10)
8            sum_of_digits+=r
9            prod_of_digits*=r
10        
11        return n %(sum_of_digits+prod_of_digits)==0
12
13        