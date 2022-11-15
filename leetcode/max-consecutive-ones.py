from lc import *

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(len(list(g))*c for c,g in groupby(nums))

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
