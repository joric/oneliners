from lc import *

# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/discuss/188642/Python-1-line-TLE

# TLE
class Solution:
    def findKthNumber(self, n, k):
        return sorted(range(1,n+1), key=str)[k-1]

# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/discuss/222264/short-python

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        c = 1 
        while k>1:
            s = 0
            a=b=c
            while a <= n:
                s += min(b,n)-a+1
                a *= 10 
                b = b*10+9
            if k>s:
                c += 1
                k -= s 
            else:
                c *= 10
                k -= 1
        return c

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        c = 1 
        while k>1:
            s = (f:=lambda s,a,b,c:a<=n and f(s+min(b,n)-a+1,a*10,b*10+9,c)or s)(0,c,c,c)
            if k>s:
                c += 1
                k -= s 
            else:
                c *= 10
                k -= 1
        return c

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        return(g:=lambda c,k:k>1 and(k>(s:=(f:=lambda s,a,b,c:a<=n and f(s+min(b,n)-a+1,a*10,b*10+9,c)or s)(0,c,c,c))and g(c+1,k-s)or g(c*10,k-1))or c)(1,k)

# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/discuss/1608540/Python3-traverse-denary-trie

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        x = 1
        while k > 1:
            c = (f:=lambda x,r,d:x<=n and f(x*10,r+min(n-x+1,d),d*10)or r)(x,0,1)
            if k > c:
                k -= c
                x += 1
            else:
                k -= 1
                x *= 10
        return x

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        return(g:=lambda k,x:k>1 and(k>(c:=(f:=lambda x,r,d:x<=n and f(x*10,r+min(n-x+1,d),d*10)or r)(x,0,1))and g(k-c,x+1)or g(k-1,x*10))or x)(k,1)

test('''
440. K-th Smallest in Lexicographical Order
Hard

774

90

Add to List

Share
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

 

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1
 

Constraints:

1 <= k <= n <= 109
Accepted
24,392
Submissions
74,402
''')
