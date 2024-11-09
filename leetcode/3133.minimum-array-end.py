from lc import *

# https://leetcode.com/problems/minimum-array-end/discuss/5097071/Python-one-line

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        return sum(2**b for i,b in enumerate([i for i in range(31)if 2**i&x==0]+[*range(31,64)])if~-n&2**i)+x

# https://leetcode.com/problems/minimum-array-end/discuss/5081947/JavaC%2B%2BPython-Bits-Manipulation

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        b = 1
        for i in range(64):
            if b & x == 0:
                x |= (n & 1) * b
                n >>= 1
            b <<= 1
        return x

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n-=1;b=1;[(b&x==0 and(x:=x|(n&1)*b,n:=n//2),b:=b*2)for i in range(64)];return x

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        for i in range(64):
            if (x >> i) & 1 == 0:
                x |= (n & 1) << i
                n >>= 1
        return x

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n-=1;[(0==1&(x>>i)and(x:=x|(n&1)<<i,n:=n//2))for i in range(64)];return x

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n-=1;[(x:=x|(n&1)<<i,n:=n//2)for i in range(64)if x>>i&1<1];return x

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        return(f:=lambda a,b:b and 2*f(a>>-~-b%2,b//2)|(a|b)&1 or a)(n-1,x)

test('''
3133. Minimum Array End
Medium

211

14

Add to List

Share
You are given two integers n and x. You have to construct an array of positive integers nums of size n where for every 0 <= i < n - 1, nums[i + 1] is greater than nums[i], and the result of the bitwise AND operation between all elements of nums is x.

Return the minimum possible value of nums[n - 1].

 

Example 1:

Input: n = 3, x = 4

Output: 6

Explanation:

nums can be [4,5,6] and its last element is 6.

Example 2:

Input: n = 2, x = 7

Output: 15

Explanation:

nums can be [7,15] and its last element is 15.

 

Constraints:

1 <= n, x <= 108
Accepted
14,657
Submissions
38,204
''')
