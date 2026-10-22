from lc import *

# https://leetcode.com/problems/maximum-k-to-sort-a-permutation/solutions/7088305/python-one-line-by-ante-nxny/?envType=daily-question&envId=2026-10-23

class Solution:
    def sortPermutation(self, a: List[int]) -> int:
        return(lambda x: reduce(and_,x)if x else 0)((lambda t:[x for i,x in enumerate(a)if x!=t[i]])(sorted(a)))

class Solution:
    def sortPermutation(self, a: List[int]) -> int:
        return(x:=[x for x,y in zip(a,sorted(a))if x!=y])and reduce(and_,x)or 0

class Solution:
    def sortPermutation(self, a: List[int]) -> int:
        return reduce(and_,[x for x,y in zip(a,sorted(a))if x!=y]or[0])

test('''
3644. Maximum K to Sort a Permutation
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums of length n, where nums is a permutation of the numbers in the range [0..n - 1].

You may swap elements at indices i and j only if nums[i] AND nums[j] == k, where AND denotes the bitwise AND operation and k is a non-negative integer.

Return the maximum value of k such that the array can be sorted in non-decreasing order using any number of such swaps. If nums is already sorted, return 0.

 

Example 1:

Input: nums = [0,3,2,1]

Output: 1

Explanation:

Choose k = 1. Swapping nums[1] = 3 and nums[3] = 1 is allowed since nums[1] AND nums[3] == 1, resulting in a sorted permutation: [0, 1, 2, 3].

Example 2:

Input: nums = [0,1,3,2]

Output: 2

Explanation:

Choose k = 2. Swapping nums[2] = 3 and nums[3] = 2 is allowed since nums[2] AND nums[3] == 2, resulting in a sorted permutation: [0, 1, 2, 3].

Example 3:

Input: nums = [3,2,1,0]

Output: 0

Explanation:

Only k = 0 allows sorting since no greater k allows the required swaps where nums[i] AND nums[j] == k.

Other examples:

Input: nums = [2,0,1]
Output: 0

Constraints:

1 <= n == nums.length <= 105
0 <= nums[i] <= n - 1
nums is a permutation of integers from 0 to n - 1.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
34,188/91.1K
Acceptance Rate
37.5%
Topics
Staff
Array
Bit Manipulation
Weekly Contest 462
icon
Companies
Hint 1
Take the bitwise AND of all elements that are not in their correct position.
''')
