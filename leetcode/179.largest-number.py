from lc import *

# https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, a: List[int]) -> str:
        return str(int(''.join(sorted(map(str,a),key=lambda s:s*9)[::-1])))

test('''
179. Largest Number
Medium

8109

678

Add to List

Share
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
Accepted
507,029
Submissions
1,373,251
''')
