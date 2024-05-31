from lc import *

# https://leetcode.com/problems/single-number-iii/discuss/931421/Python-One-Liner

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a = b = c = 0
        for x in nums:
            c ^= x
        r = c & (-c)
        for x in nums:
            if x & r:
                a ^= x
            else:
                b ^= x
        return a, b

class Solution:
    def singleNumber(self, n: List[int]) -> List[int]:
        return map(itemgetter(0),Counter(n).most_common()[-2:])

class Solution:
    def singleNumber(self, n: List[int]) -> List[int]:
        return[x[0]for x in Counter(n).most_common()[-2:]]

class Solution:
    def singleNumber(self, n: List[int]) -> List[int]:
        return[x[0]for x in Counter(n).items()if x[1]<2]

class Solution:
    def singleNumber(self, n: List[int]) -> List[int]:
        return[u for u,v in Counter(n).items()if v<2]

test('''
260. Single Number III
Medium

5685

234

Add to List

Share
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]
 

Constraints:

2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice, only two integers will appear once.
Accepted
352,900
Submissions
515,737
''')
