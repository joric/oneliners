from lc import *

# https://leetcode.com/problems/number-of-unique-xor-triplets-ii/solutions/6644383/one-line-solution-by-xxxxkav-0gcp/?envType=daily-question&envId=2026-07-23

class Solution:
    def uniqueXorTriplets(self, a: List[int]) -> int:
        return len({x^y for x,y in product({x^y for x,y in combinations_with_replacement(a,2)},a)})

class Solution: # TLE
    def uniqueXorTriplets(self, a: List[int]) -> int:
        return len({x^y^z for x,y,z in product(a,a,a)})

class Solution:
    def uniqueXorTriplets(self, a: List[int]) -> int:
        s={*a};p={x^y for x in s for y in s};return len({x^y for x in s for y in p})

class Solution:
    def uniqueXorTriplets(self, a: List[int]) -> int:
        s={*a};return len({x^y for y in{x^y for x in s for y in s}for x in s})

class Solution:
    def uniqueXorTriplets(self, a: List[int]) -> int:
        return len({x^y for y in{x^y for x in a for y in a}for x in a})

class Solution:
    def uniqueXorTriplets(self, a: List[int]) -> int:
        f=lambda s:{*starmap(xor,product(a,s))};return len(f(f(a)))

test('''
3514. Number of Unique XOR Triplets II
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.

Return the number of unique XOR triplet values from all possible triplets (i, j, k).

 

Example 1:

Input: nums = [1,3]

Output: 2

Explanation:

The possible XOR triplet values are:

(0, 0, 0) → 1 XOR 1 XOR 1 = 1
(0, 0, 1) → 1 XOR 1 XOR 3 = 3
(0, 1, 1) → 1 XOR 3 XOR 3 = 1
(1, 1, 1) → 3 XOR 3 XOR 3 = 3
The unique XOR values are {1, 3}. Thus, the output is 2.

Example 2:

Input: nums = [6,7,8,9]

Output: 4

Explanation:

The possible XOR triplet values are {6, 7, 8, 9}. Thus, the output is 4.

 

Constraints:

1 <= nums.length <= 1500
1 <= nums[i] <= 1500
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
14,961/45.5K
Acceptance Rate
32.9%
Topics
Staff
Array
Math
Bit Manipulation
Enumeration
Biweekly Contest 154
icon
Companies
Hint 1
What is the maximum possible XOR value achievable by any triplet?
Hint 2
Let the maximum possible XOR value be stored in max_xor.
Hint 3
For each index i, consider all pairs of indices (j, k) such that i <= j <= k. For each such pair, compute the triplet XOR as nums[i] XOR nums[j] XOR nums[k].
Hint 4
You can optimize the calculation by precomputing or reusing intermediate XOR results. For example, after fixing an index i, compute XORs of pairs (j, k) in O(n2) time instead of checking all three indices independently.
Hint 5
Finally, count the number of unique XOR values obtained from all triplets.
''')
