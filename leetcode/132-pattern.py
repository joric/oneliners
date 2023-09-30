from lc import *

# https://leetcode.com/problems/132-pattern/discuss/699425/Python-in-6-short-lines-beats-95

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        a,s = -inf,[]
        for v in nums[::-1]:
            if v < a:
                return True
            while s and s[-1] < v:
                a = s.pop()
            s.append(v)

class Solution:
    def find132pattern(self, n: List[int]) -> bool:
        a,s=-inf,[];return any(v<a or not(a:=(f:=lambda a:s and v>s[-1]and f(s.pop())or a)(a),s.append(v))for v in n[::-1])

test('''
456. 132 Pattern
Medium

6118

340

Add to List

Share
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

Constraints:

n == nums.length
1 <= n <= 2 * 10^5
-10^9 <= nums[i] <= 10^9
Accepted
187,866
Submissions
577,280
''')

