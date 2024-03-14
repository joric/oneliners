from lc import *

#  https://leetcode.com/problems/binary-subarrays-with-sum/discuss/186683/C%2B%2BJavaPython-Sliding-Window-O(1)-Space

class Solution:
    def numSubarraysWithSum(self, n: List[int], g: int) -> int:
        p = r = 0
        c = Counter([0])
        for i in n:
            p += i
            r += c[p-g]
            c[p] += 1
        return r

class Solution:
    def numSubarraysWithSum(self, n: List[int], g: int) -> int:
        p,c=0,Counter([0]);return sum((c[(p:=p+i)-g],c.update([p]))[0]for i in n)

# https://leetcode.com/problems/binary-subarrays-with-sum/discuss/186815/Simple-python-solution

class Solution:
    def numSubarraysWithSum(self, n: List[int], g: int) -> int:
        p = r = 0
        c = Counter()
        for x in n:
            c[p+g] += 1
            p += x
            r += c[p]
        return r

class Solution:
    def numSubarraysWithSum(self, n: List[int], g: int) -> int:
        p,c=0,Counter();return sum(c.update([p+g])or c[p:=p+x]for x in n)

test('''
930. Binary Subarrays With Sum
Medium

2818

78

Add to List

Share
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
 

Constraints:

1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length
Accepted
99,836
Submissions
177,057
''')
