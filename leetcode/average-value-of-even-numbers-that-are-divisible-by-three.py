from lc import *

class Solution1:
    def averageValue(self, nums: List[int]) -> int:
        s = c = 0
        for x in nums:
            if x%2==0 and x%3==0:
                s += x
                c += 1
        return s // c if c else 0

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        return (lambda s,c:c and s//c)(*reduce(lambda a,b:(a[0]+b,a[1]+1),(x for x in nums if not x%6),[0,0]))

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        return ((v:=[x for x in nums if not x%6]) or 0) and sum(v)//len(v)

test('''

2455. Average Value of Even Numbers That Are Divisible by Three
Easy

Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.

Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.

Example 1:

Input: nums = [1,3,6,10,12,15]
Output: 9
Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.

Example 2:

Input: nums = [1,2,4,7,10]
Output: 0
Explanation: There is no single number that satisfies the requirement, so return 0.

Example 3:

Input: nums = [4,4,9,10]
Output: 0 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000


''')
