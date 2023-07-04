from lc import *

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for x in nums:
            ones = (ones ^ x) & ~twos # if occured twice, removed from ones
            twos = (twos ^ x) & ~ones # if occured thrice, removed from ones and twos
        return ones

class Solution:
    def singleNumber(self, n: List[int]) -> int:
        return [i for i in set(n) if n.count(i)<2][0]

class Solution:
    def singleNumber(self, n: List[int]) -> int:
        return (Counter(n).most_common()[-1])[0]

class Solution:
    def singleNumber(self, n: List[int]) -> int:
        return (sum(set(n))*3-sum(n))//2

class Solution:
    def singleNumber(self, n: List[int]) -> int:
        return (sum({*n})*3-sum(n))//2

test('''
137. Single Number II
Medium

5820

558

Add to List

Share
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99

Example 3:
Input: nums = [-2,-2,1,1,4,1,4,4,-4,-2]
Output: -4

Constraints:

1 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
Each element in nums appears exactly three times except for one element which appears once.
''')
