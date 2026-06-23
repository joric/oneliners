from lc import *

# https://leetcode.com/problems/number-of-zigzag-arrays-ii/solutions/7231153/python-fast-pow-by-lee215-nlwo/

import numpy as np

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        d = 10**9+7
        k = r - l + 1
        m = np.array([[int(i+j+1<k)for j in range(k)]for i in range(k)],dtype=object)
        t = np.ones((1,k),dtype=object)
        n -= 1
        while n:
            if n&1:
                t=(t@m)%d
            m = (m @ m) % d
            n >>= 1
        return int(t.sum()*2%d)


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        p=__import__('numpy')
        d = 10**9+7
        k = r - l + 1
        m = p.array([[int(i+j+1<k)for j in range(k)]for i in range(k)],dtype=object)
        t = p.ones((1,k),dtype=object)
        n -= 1
        while n:
            if n&1:
                t=(t@m)%d
            m = (m @ m) % d
            n >>= 1
        return int(t.sum()*2%d)

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        p=__import__('numpy');d=10**9+7;v=range(k:=r-l+1);f=lambda x,m,t:x<1 and int(t.sum()*2%d)or f(x>>1,(m@m)%d,(t@m)%d if x&1 else t);return f(n-1,p.array([[int(i+j+1<k)for j in v]for i in v],object),p.ones((1,k),object))

test('''
3700. Number of ZigZag Arrays II
Hard
Topics
premium lock icon
Companies
Hint
You are given three integers n, l, and r.

A ZigZag array of length n is defined as follows:

Each element lies in the range [l, r].
No two adjacent elements are equal.
No three consecutive elements form a strictly increasing or strictly decreasing sequence.
Return the total number of valid ZigZag arrays.

Since the answer may be large, return it modulo 109 + 7.

A sequence is said to be strictly increasing if each element is strictly greater than its previous one (if exists).

A sequence is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).

 

Example 1:

Input: n = 3, l = 4, r = 5

Output: 2

Explanation:

There are only 2 valid ZigZag arrays of length n = 3 using values in the range [4, 5]:

[4, 5, 4]
[5, 4, 5]
Example 2:

Input: n = 3, l = 1, r = 3

Output: 10

Explanation:

​​​​​​​There are 10 valid ZigZag arrays of length n = 3 using values in the range [1, 3]:

[1, 2, 1], [1, 3, 1], [1, 3, 2]
[2, 1, 2], [2, 1, 3], [2, 3, 1], [2, 3, 2]
[3, 1, 2], [3, 1, 3], [3, 2, 3]
All arrays meet the ZigZag conditions.

 

Constraints:

3 <= n <= 109
1 <= l < r <= 75​​​​​​​
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
14,980/26K
Acceptance Rate
57.6%
Topics
Principal
Math
Dynamic Programming
Weekly Contest 469
icon
Companies
Hint 1
Use matrix exponentiation
Hint 2
Encode states in a vector of length 2*m where m = r - l + 1: first m entries = "next compare = down" for values, next m = "next compare = up".
Hint 3
Build a transition matrix T (size 2*m × 2*m): from an up,x state go to down,y for every y > x, and from down,x go to up,y for every y < x.
Hint 4
Use fast matrix exponentiation to compute T^(n-1), apply it to the initial vector (ones in the block for starting up and separately for starting down), sum final entries, and add both results (for n=1 return m).
''')
