from lc import *

# https://leetcode.com/problems/maximum-average-subarray-i/discuss/105435/2-lines-Python-2-versions

class Solution:
    def findMaxAverage(self, n: List[int], k: int) -> float:
        s=__import__('numpy').cumsum([0]+n);return int(max(s[k:]-s[:-k]))/k

class Solution:
    def findMaxAverage(self, n: List[int], k: int) -> float:
        return max(map(sub,(s:=[0]+[*accumulate(n)])[k:],s))/k

class Solution:
    def findMaxAverage(self, n: List[int], k: int) -> float:
        s=[0]+[*accumulate(n)];return max(map(sub,s[k:],s))/k

test('''
643. Maximum Average Subarray I
Easy

2472

198

Add to List

Share
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 10^5
-104 <= nums[i] <= 10^4
Accepted
217,650
Submissions
498,069
Seen this question in a real interview before?

Yes

No
Maximum Average Subarray II
Hard
K Radius Subarray Averages
''')

