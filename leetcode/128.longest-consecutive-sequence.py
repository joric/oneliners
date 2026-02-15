from lc import *

# https://leetcode.com/problems/longest-consecutive-sequence/solutions/5023956/one-line-solution-by-mikposp-9ixr/

class Solution:
    def longestConsecutive(self, a: List[int]) -> int:
        maxLen = 0
        a = {*a}
        for v in a:
            if v-1 not in a:
                curLen = 0
                while v in a:
                    curLen += 1
                    v += 1
                maxLen = max(maxLen, curLen)
        return maxLen

class Solution:
    def longestConsecutive(self, a: List[int]) -> int:
        return (a:={*a}) and max(sum(1 for _ in takewhile(a.__contains__,count(v))) for v in a if v-1 not in a) or 0

class Solution:
    def longestConsecutive(self, a: List[int]) -> int:
        return (a:={*a}) and max(len([*takewhile(a.__contains__,count(v))]) for v in a if v-1 not in a) or 0

class Solution:
    def longestConsecutive(self, a: List[int]) -> int:
        a={*a};return max(len([*takewhile(a.__contains__,count(v))])for v in a if v-1 not in a)or 0

test('''
128. Longest Consecutive Sequence
Solved
Medium
Topics
premium lock icon
Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
3,139,629/6.7M
Acceptance Rate
47.0%
Topics
Array
Hash Table
Union-Find
icon
Companies
Similar Questions
Binary Tree Longest Consecutive Sequence
Medium
Find Three Consecutive Integers That Sum to a Given Number
Medium
Maximum Consecutive Floors Without Special Floors
Medium
Length of the Longest Alphabetical Continuous Substring
Medium
Find the Maximum Number of Elements in Subset
Medium
''')
