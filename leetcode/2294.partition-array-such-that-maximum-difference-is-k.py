from lc import *

# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/solutions/6855596/one-line-solution/?envType=daily-question&envId=2025-06-19

class Solution:
    def partitionArray(self, a: List[int], k: int) -> int:
        a.sort();q=a.pop(0);return 1+len([q:=v for v in a if v>q+k])

class Solution:
    def partitionArray(self, a: List[int], k: int) -> int:
        return len({*accumulate(sorted(a),lambda q,v:(q,v)[v-q>k])})

class Solution:
    def partitionArray(self, a: List[int], k: int) -> int:
        a.sort();q=a[0];return len({q:=(q,v)[v-q>k]for v in a})

test('''
2294. Partition Array Such That Maximum Difference Is K
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and an integer k. You may partition nums into one or more subsequences such that each element in nums appears in exactly one of the subsequences.

Return the minimum number of subsequences needed such that the difference between the maximum and minimum values in each subsequence is at most k.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [3,6,1,2,5], k = 2
Output: 2
Explanation:
We can partition nums into the two subsequences [3,1,2] and [6,5].
The difference between the maximum and minimum value in the first subsequence is 3 - 1 = 2.
The difference between the maximum and minimum value in the second subsequence is 6 - 5 = 1.
Since two subsequences were created, we return 2. It can be shown that 2 is the minimum number of subsequences needed.
Example 2:

Input: nums = [1,2,3], k = 1
Output: 2
Explanation:
We can partition nums into the two subsequences [1,2] and [3].
The difference between the maximum and minimum value in the first subsequence is 2 - 1 = 1.
The difference between the maximum and minimum value in the second subsequence is 3 - 3 = 0.
Since two subsequences were created, we return 2. Note that another optimal solution is to partition nums into the two subsequences [1] and [2,3].
Example 3:

Input: nums = [2,2,4,5], k = 0
Output: 3
Explanation:
We can partition nums into the three subsequences [2,2], [4], and [5].
The difference between the maximum and minimum value in the first subsequences is 2 - 2 = 0.
The difference between the maximum and minimum value in the second subsequences is 4 - 4 = 0.
The difference between the maximum and minimum value in the third subsequences is 5 - 5 = 0.
Since three subsequences were created, we return 3. It can be shown that 3 is the minimum number of subsequences needed.


Other examples:

Input: nums = [3,1,3,4,2], k = 0
Output: 4

Input: nums = [0], k = 1
Output: 1

Input: nums = [0], k = 5
Output: 1

Input: nums = [0,1,2,3], k = 1
Output: 2

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
0 <= k <= 105
Seen this question in a real interview before?
1/5
Yes
No
Accepted
52,170/69.9K
Acceptance Rate
74.6%
Topics
Array
Greedy
Sorting
icon
Companies
Hint 1
Which values in each subsequence matter? The only values that matter are the maximum and minimum values.
Hint 2
Let the maximum and minimum values of a subsequence be Max and Min. It is optimal to place all values in between Max and Min in the original array in the same subsequence as Max and Min.
Hint 3
Sort the array.
Similar Questions
Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Medium
Maximum Beauty of an Array After Applying Operation
Medium
''')
