from lc import *

# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/solutions/7331168/one-line-solution-by-gbaka-n67t/?envType=daily-question&envId=2026-05-29
# apparently biweekly 140

class Solution:
    def minElement(self, a: List[int]) -> int:
        return min(sum(map(int,str(x)))for x in a)

test('''
3300. Minimum Element After Replacement With Digit Sum
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

You replace each element in nums with the sum of its digits.

Return the minimum element in nums after all replacements.

 

Example 1:

Input: nums = [10,12,13,14]

Output: 1

Explanation:

nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.

Example 2:

Input: nums = [1,2,3,4]

Output: 1

Explanation:

nums becomes [1, 2, 3, 4] after all replacements, with minimum element 1.

Example 3:

Input: nums = [999,19,199]

Output: 10

Explanation:

nums becomes [27, 10, 19] after all replacements, with minimum element 10.


Other examples:

Input: nums = [98,100]
Output: 1

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 104
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
73,961/87.2K
Acceptance Rate
84.8%
Topics
Mid Level
Array
Math
Biweekly Contest 140
icon
Companies
Hint 1
Convert to string and calculate the sum for each element.
Similar Questions
Sum of Digits of String After Convert
Easy
''')
