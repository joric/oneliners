from lc import *

# https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/solutions/6643204/iteration-boundary_consideration-by-zhan-znkn/

class Solution:
    def maxProduct(self, a: List[int], k: int, l: int) -> int:
        r = -1
        @cache
        def f(i,s,m,o,e):
            nonlocal r
            if r == l or r >= 0 and m > l:
                return
            if i == len(a):
                if s == k and m <= l and not e:
                    r = max(r, m)
                return
            f(i+1,s,m,o,e)
            f(i+1,s+(a[i] if not o else -a[i]), min(m*a[i],l+1),not o,0)
        f(0,0,1,0,1)
        f.cache_clear()
        return r

class Solution:
    def maxProduct(self, a: List[int], k: int, l: int) -> int:
        @cache
        def f(i,s,m,o,e,r):
            if r == l or r >= 0 and m > l:
                return r
            if i == len(a):
                if s == k and m <= l and not e:
                    return max(r, m)
                return r
            return f(i+1,s+(a[i]if 1-o else -a[i]),min(m*a[i],l+1),1-o,0,f(i+1,s,m,o,e,r))
        return(f(0,0,1,0,1,-1),f.cache_clear())[0]

class Solution:
    def maxProduct(self, a: List[int], k: int, l: int) -> int:
        f=cache(lambda i,s,m,o,e,r:r if r==l or~r and m>l else(max(r,m)if s==k and m<=l and e<1 else r)if i==len(a)else f(i+1,s+a[i]*(1-2*o),min(m*a[i],l+1),1-o,0,f(i+1,s,m,o,e,r)));return(f(0,0,1,0,1,-1),f.cache_clear())[0]

class Solution:
    def maxProduct(self, a: List[int], k: int, l: int) -> int:
        f=cache(lambda i,s,m,o,e,r:r if r==l or~r<0<m-l else(max(r,m)if s==k and e<1>m-l else r)if i==len(a)else f(i+1,s+a[i]*(1-2*o),min(m*a[i],l+1),1-o,0,f(i+1,s,m,o,e,r)));return(f(0,0,1,0,1,-1),f.cache_clear())[0]

test('''
3509. Maximum Product of Subsequences With an Alternating Sum Equal to K
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and two integers, k and limit. Your task is to find a non-empty subsequence of nums that:

Has an alternating sum equal to k.
Maximizes the product of all its numbers without the product exceeding limit.
Return the product of the numbers in such a subsequence. If no subsequence satisfies the requirements, return -1.

The alternating sum of a 0-indexed array is defined as the sum of the elements at even indices minus the sum of the elements at odd indices.

 

Example 1:

Input: nums = [1,2,3], k = 2, limit = 10

Output: 6

Explanation:

The subsequences with an alternating sum of 2 are:

[1, 2, 3]
Alternating Sum: 1 - 2 + 3 = 2
Product: 1 * 2 * 3 = 6
[2]
Alternating Sum: 2
Product: 2
The maximum product within the limit is 6.

Example 2:

Input: nums = [0,2,3], k = -5, limit = 12

Output: -1

Explanation:

A subsequence with an alternating sum of exactly -5 does not exist.

Example 3:

Input: nums = [2,2,3,3], k = 0, limit = 9

Output: 9

Explanation:

The subsequences with an alternating sum of 0 are:

[2, 2]
Alternating Sum: 2 - 2 = 0
Product: 2 * 2 = 4
[3, 3]
Alternating Sum: 3 - 3 = 0
Product: 3 * 3 = 9
[2, 2, 3, 3]
Alternating Sum: 2 - 2 + 3 - 3 = 0
Product: 2 * 2 * 3 * 3 = 36
The subsequence [2, 2, 3, 3] has the greatest product with an alternating sum equal to k, but 36 > 9. The next greatest product is 9, which is within the limit.

Other solutions:

Input: nums = [0], k = 0, limit = 10
Output: 0

Constraints:

1 <= nums.length <= 150
0 <= nums[i] <= 12
-105 <= k <= 105
1 <= limit <= 5000
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
6,561/48.4K
Acceptance Rate
13.6%
Topics
Senior Staff
Array
Hash Table
Dynamic Programming
Weekly Contest 444
icon
Companies
Hint 1
Use dynamic programming.
Hint 2
Save all possible products with a particular sum.
Hint 3
Handle the case where a subsequence has a product of 0 and an alternating sum of k.
Similar Questions
Maximum Alternating Subsequence Sum
Medium
''')
