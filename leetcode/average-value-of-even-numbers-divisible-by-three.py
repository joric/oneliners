from lc import *

class Solution:
    def averageValue(self, nums):
        t = c = 0
        for x in nums:
            if x%2==0 and x%3==0:
                t += x
                c += 1
        return t // c if c else 0

test('''

6220. Average value of even numbers that are divisible by three

Example 1:

Input: nums = [1,3,6,10,12,15]
Output: 9

Example 2:

Input: nums = [1,2,4,7,10]
Output: 0

Example 3:

Input: nums = [4,4,9,10]
Output: 0


''')
