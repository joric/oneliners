from lc import *

# 2d dp

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[1] * (k+1) for _ in range(n+1)]
        sp = [[1] * (k+1) for _ in range(n+1)]
        N = 10**9 + 7
        for i in range(1, n+1):
            for j in range(1, k+1):
                dp[i][j] = sp[i-1][j] if j < i else (sp[i-1][j] - sp[i-1][j-i]) % N
                sp[i][j] = (sp[i][j-1] + dp[i][j]) % N
        return dp[-1][-1]

# 1d dp

class Solution():
    def kInversePairs(self, n: int, k: int) -> int:
        d = [0] + [1] * (k + 1)
        for n in range(2, n+1):
            t = [0]
            for k in range(k+1):
                v = d[k+1]
                v -= d[k-n+1] if k >= n else 0
                t.append( (t[-1] + v) )
            d = t
        return (d[k+1] - d[k]) % (10**9 + 7)  

# https://leetcode.com/problems/k-inverse-pairs-array/discuss/3832571/python.-1-line!!

class Solution:
    @cache
    def kInversePairs(self, n: int, k: int) -> int:
        return+(not k or n!=1 and(self.kInversePairs(n,k-1)+self.kInversePairs(n-1,k)-(k>=n and self.kInversePairs(n-1,k-n)))%(10**9+7))

class Solution:
    @cache
    def kInversePairs(self, n: int, k: int) -> int:
        return(k==0 or n>1 and k>0 and self.kInversePairs(n,k-1)+self.kInversePairs(n-1,k)-self.kInversePairs(n-1,k-n))%(10**9+7)

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        return(f:=cache(lambda n,k:k==0 or~-n and k>0and f(n,k-1)+f(n-1,k)-f(n-1,k-n)))(n,k)%(10**9+7)

test('''
629. K Inverse Pairs Array
Hard

1996

226

Add to List

Share
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

 

Example 1:

Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
Example 2:

Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
 

Constraints:

1 <= n <= 1000
0 <= k <= 1000
Accepted
61,409
Submissions
143,250
''')
