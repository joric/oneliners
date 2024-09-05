from lc import *

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        return max((a+i)//(i+1) for i,a in enumerate(accumulate(nums)))

test('''

2439. Minimize Maximum of Array
Medium

765

153

Add to List

Share
You are given a 0-indexed array nums comprising of n non-negative integers.

In one operation, you must:

Choose an integer i such that 1 <= i < n and nums[i] > 0.
Decrease nums[i] by 1.
Increase nums[i - 1] by 1.
Return the minimum possible value of the maximum integer of nums after performing any number of operations.

 

Example 1:

Input: nums = [3,7,1,6]
Output: 5
Explanation:
One set of optimal operations is as follows:
1. Choose i = 1, and nums becomes [4,6,1,6].
2. Choose i = 3, and nums becomes [4,6,2,5].
3. Choose i = 1, and nums becomes [5,5,2,5].
The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
Therefore, we return 5.
Example 2:

Input: nums = [10,1]
Output: 10
Explanation:
It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.
 

Constraints:

n == nums.length
2 <= n <= 105
0 <= nums[i] <= 109
Accepted
20,256
Submissions
49,517
Seen this question in a real interview before?

Yes

No
Try a binary search approach.
Perform a binary search over the minimum value that can be achieved for the maximum number of the array.
In each binary search iteration, iterate through the array backwards, greedily decreasing the current element until it is within the limit.

''')

