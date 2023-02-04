from lc import *

# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/discuss/164610/Python-DP-solution-using-Counter

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0 
        freq = [defaultdict(int) for _ in range(len(nums))] # arithmetic sub-seqs
        for i, x in enumerate(nums): 
            for ii in range(i): 
                diff = x - nums[ii]
                ans += freq[ii].get(diff, 0)
                freq[i][diff] += 1 + freq[ii][diff]
        return ans

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        r, c = 0, [Counter() for _ in range(len(nums))]
        for i, x in enumerate(nums): 
            for j in range(i):
                d = x - nums[j]
                r += c[j][d]
                c[i][d] += 1 + c[j][d]
                print(c,d,r)
        return r 

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        return (r:=0,c:=[Counter() for _ in nums]) and all((d:=x-nums[j],r:=r+c[j][d],setitem(c[i],d,1+c[i][d]+c[j][d])) for i,x in enumerate(nums) for j in range(i)) and r

test('''
446. Arithmetic Slices II - Subsequence
Hard

1738

96

Add to List

Share
Given an integer array nums, return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
The test cases are generated so that the answer fits in 32-bit integer.

 

Example 1:

Input: nums = [2,4,6,8,10]
Output: 7
Explanation: All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]

Example 2:

Input: nums = [7,7,7,7,7]
Output: 16
Explanation: Any subsequence of this array is arithmetic.
 

Constraints:

1  <= nums.length <= 1000
-2^31 <= nums[i] <= 2^31 - 1
''')
