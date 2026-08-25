from lc import *

# https://leetcode.com/problems/smallest-missing-multiple-of-k/solutions/8478952/one-line-solution-by-mikposp-wtln/?envType=daily-question&envId=2026-08-25

class Solution:
    def missingMultiple(self, a: List[int], k: int) -> int:
        return next(v for v in count(k,k)if v not in a)

class Solution:
    def missingMultiple(self, a: List[int], k: int) -> int:
        return next(dropwhile(a.count,count(k,k)))

class Solution:
    def missingMultiple(self, a: List[int], k: int) -> int:
        return min({*range(k,301,k)}-{*a})

test('''
3718. Smallest Missing Multiple of K
Easy
Topics
premium lock icon
Companies
Hint
Given an integer array nums and an integer k, return the smallest positive multiple of k that is missing from nums.

A multiple of k is any positive integer divisible by k.

 

Example 1:

Input: nums = [8,2,3,4,6], k = 2

Output: 10

Explanation:

The multiples of k = 2 are 2, 4, 6, 8, 10, 12... and the smallest multiple missing from nums is 10.

Example 2:

Input: nums = [1,4,7,10,15], k = 5

Output: 5

Explanation:

The multiples of k = 5 are 5, 10, 15, 20... and the smallest multiple missing from nums is 5.

 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
1 <= k <= 100
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
51,519/81.8K
Acceptance Rate
63.0%
Topics
Mid Level
Array
Hash Table
Weekly Contest 472
icon
Companies
Hint 1
Add the values in nums to a hash set
Hint 2
Iterate through the positive multiples of k and return the first one not in the hash set
''')
