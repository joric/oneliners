from lc import *

# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/solutions/6884349/one-line-solution/?envType=daily-question&envId=2025-06-28

class Solution:
    def maxSubsequence(self, a: List[int], k: int) -> List[int]:
        return[v for _,v in sorted(nlargest(k,enumerate(a),itemgetter(1)))]

class Solution:
    def maxSubsequence(self, a: List[int], k: int) -> List[int]:
        return[*zip(*sorted(nlargest(k,enumerate(a),itemgetter(1))))][1]

test('''
2099. Find Subsequence of Length K With the Largest Sum
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.
Example 2:

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.
Example 3:

Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].


Other examples:

Input: nums = [50,-75], k = 2
Output: [50,-75]

Constraints:

1 <= nums.length <= 1000
-105 <= nums[i] <= 105
1 <= k <= nums.length
Seen this question in a real interview before?
1/5
Yes
No
Accepted
70,167/151.6K
Acceptance Rate
46.3%
Topics
Array
Hash Table
Sorting
Heap (Priority Queue)
icon
Companies
Hint 1
From a greedy perspective, what k elements should you pick?
Hint 2
Could you sort the array while maintaining the index?
Similar Questions
Kth Largest Element in an Array
Medium
Maximize Sum Of Array After K Negations
Easy
Sort Integers by The Number of 1 Bits
Easy
Minimum Difference in Sums After Removal of Elements
Hard
''')
