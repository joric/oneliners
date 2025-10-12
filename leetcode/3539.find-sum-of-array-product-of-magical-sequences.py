from lc import *

# https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/description/?envType=daily-question&envId=2025-10-12

MOD = 10**9 + 7
class Solution:
    def magicalSum(self, M: int, K: int, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(m,k,i,flag):
            if m<0 or k<0 or m+flag.bit_count() < k: return 0
            if m==0:
                if k==flag.bit_count(): return 1
                else: return 0
            if i>=len(nums): return 0
            res=0
            for c in range(m+1):
                mul=math.comb(m,c)*pow(nums[i], c, MOD)%MOD
                f2 = flag+c
                res += mul*dp(m-c, k-(f2%2), i+1, f2//2)
            return res%MOD
        return dp(M,K,0,0)

class Solution:
    def magicalSum(self, m: int, k: int, a: List[int]) -> int:
        @cache
        def f(x,y,i,b):
            if x < 0 or y < 0 or x + b.bit_count() < y:
                return 0
            if x == 0:
                return int(y == b.bit_count())
            return i<len(a) and sum(comb(x,c)*pow(a[i],c)*f(x-c,y-((d:=b+c)%2),i+1,d//2)for c in range(x+1))%(10**9+7)
        return f(m,k,0,0)

class Solution:
    def magicalSum(self, m: int, k: int, a: List[int]) -> int:
        return(f:=cache(lambda x,y,i,b:y>-1<=x+(t:=b.bit_count())and(i<len(a)and sum(comb(x,c)*a[i]**c*f(x-c,y-((d:=b+c)%2),i+1,d//2)for c in range(x+1))%(10**9+7)if x else y==t)))(m,k,0,0)

test('''
3539. Find Sum of Array Product of Magical Sequences
Hard
Topics
premium lock icon
Companies
Hint
You are given two integers, m and k, and an integer array nums.

A sequence of integers seq is called magical if:
seq has a size of m.
0 <= seq[i] < nums.length
The binary representation of 2seq[0] + 2seq[1] + ... + 2seq[m - 1] has k set bits.
The array product of this sequence is defined as prod(seq) = (nums[seq[0]] * nums[seq[1]] * ... * nums[seq[m - 1]]).

Return the sum of the array products for all valid magical sequences.

Since the answer may be large, return it modulo 109 + 7.

A set bit refers to a bit in the binary representation of a number that has a value of 1.

 

Example 1:

Input: m = 5, k = 5, nums = [1,10,100,10000,1000000]

Output: 991600007

Explanation:

All permutations of [0, 1, 2, 3, 4] are magical sequences, each with an array product of 1013.

Example 2:

Input: m = 2, k = 2, nums = [5,4,3,2,1]

Output: 170

Explanation:

The magical sequences are [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 4], [4, 0], [4, 1], [4, 2], and [4, 3].

Example 3:

Input: m = 1, k = 1, nums = [28]

Output: 28

Explanation:

The only magical sequence is [0].

Other examples:

Input: m = 2, k = 1, nums = [63]
Output: 3969


Constraints:

1 <= k <= m <= 30
1 <= nums.length <= 50
1 <= nums[i] <= 108
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
5,480/12.9K
Acceptance Rate
42.4%
Topics
Array
Math
Dynamic Programming
Bit Manipulation
Combinatorics
Bitmask
Weekly Contest 448
icon
Companies
Hint 1
Use Dynamic Programming
Hint 2
Let dp[i][j][mask] be the state after choosing i numbers (indices)
Hint 3
The partial sum S = 2^(seq[0]) + 2^(seq[1]) + ... + 2^(seq[i - 1]) has produced exactly j set bits once you’ve fully propagated any carries
Hint 4
The mask represents the "window" of lower-order bits from S that have not yet been fully processed (i.e. bits that might later create new set bits when additional terms are added)
Hint 5
Use combinatorics
Hint 6
How many ways are there to permute a sequence of entities where some are repetitive?
Similar Questions
Product of Array Except Self
Medium
Smallest Number With All Set Bits
Easy
''')
