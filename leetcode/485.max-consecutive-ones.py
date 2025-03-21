from lc import *

# https://leetcode.com/problems/max-consecutive-ones

class Solution:
    def findMaxConsecutiveOnes(self, n: List[int]) -> int:
        return max(sum(c for _ in g)for c,g in groupby(n))

class Solution:
    def findMaxConsecutiveOnes(self, n: List[int]) -> int:
        return max(c*len([*g])for c,g in groupby(n))

test('''

485. Max Consecutive Ones
Easy

3624

414

Add to List

Share
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.

''')