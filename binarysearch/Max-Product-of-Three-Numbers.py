from lc import *

class Solution:
    def solve(self, nums):
        l1 = l2 = l3 = -inf
        s1 = s2 = inf
        for n in nums:
            l1, l2, l3 = max(l1, n), max(l2, min(n, l1)), max(l3, min(l2, n))
            s1, s2 = min(s1, n), min(s2, max(n, s1))
        return max(l1*l2*l3, s1*s2*l1)

class Solution:
    def solve(self, nums):
        return max((v:=sorted(nums))[-1]*v[-2]*v[-3], v[0]*v[1]*v[-1])

test('''

Given a list of integers nums, find the largest product of three distinct elements.

Constraints

3 <= n <= 100,000 where n is the length of nums

https://binarysearch.com/problems/Max-Product-of-Three-Numbers

Examples

Example 1

Input: nums = [5, 4, 1, 3, -2, -2]
Output: 60

Explanation

We can multiply 5 * 4 * 3

Example 2

Input: nums = [-3, 1, 1, 0]
Output: 0

Explanation

We can multiply 1 * 1 * 0

''')

