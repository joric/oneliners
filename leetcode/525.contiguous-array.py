from lc import *

# https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, n: List[int]) -> int:
        h = {}
        c = r = 0
        for i in range(len(n)):
            c += 1 if n[i] else -1
            if c==0:
                r = i + 1
            if c in h:
                r = max(r, i - h[c])
            else:
                h[c] = i
        return r

# https://leetcode.com/problems/contiguous-array/discuss/99658/Python-and-Java-with-little-tricks-(incl.-a-oneliner-%3A-)

class Solution:
    def findMaxLength(self, n: List[int]) -> int:
        d = {0:-1}
        s = r = 0
        for i,x in enumerate(n):
            s += x - .5
            r = max(r,i-d.setdefault(s,i))
        return r

class Solution:
    def findMaxLength(self, n: List[int]) -> int:
        d,s={0:-1},0;return max(i-d.setdefault(s:=s+x-.5,i)for i,x in enumerate(n))

test('''
525. Contiguous Array
Medium

6975

288

Add to List

Share
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
Accepted
332,008
Submissions
708,028
''')