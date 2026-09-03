from lc import *

# https://leetcode.com/problems/smallest-stable-index-i/solutions/8498365/one-line-solution-by-mikposp-bhu9/?envType=daily-question&envId=2026-09-04

class Solution:
    def firstStableIndex(self, a:list[int],k:int)->int:
        return next((i for i in range(len(a))if max(a[:i+1])-min(a[i:])<=k),-1)

test('''
3903. Smallest Stable Index I
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array nums of length n and an integer k.

For each index i, define its instability score as max(nums[0..i]) - min(nums[i..n - 1]).

In other words:

max(nums[0..i]) is the largest value among the elements from index 0 to index i.
min(nums[i..n - 1]) is the smallest value among the elements from index i to index n - 1.
An index i is called stable if its instability score is less than or equal to k.

Return the smallest stable index. If no such index exists, return -1.

 

Example 1:

Input: nums = [5,0,1,4], k = 3

Output: 3

Explanation:

At index 0: The maximum in [5] is 5, and the minimum in [5, 0, 1, 4] is 0, so the instability score is 5 - 0 = 5.
At index 1: The maximum in [5, 0] is 5, and the minimum in [0, 1, 4] is 0, so the instability score is 5 - 0 = 5.
At index 2: The maximum in [5, 0, 1] is 5, and the minimum in [1, 4] is 1, so the instability score is 5 - 1 = 4.
At index 3: The maximum in [5, 0, 1, 4] is 5, and the minimum in [4] is 4, so the instability score is 5 - 4 = 1.
This is the first index with an instability score less than or equal to k = 3. Thus, the answer is 3.
Example 2:

Input: nums = [3,2,1], k = 1

Output: -1

Explanation:

At index 0, the instability score is 3 - 1 = 2.
At index 1, the instability score is 3 - 1 = 2.
At index 2, the instability score is 3 - 1 = 2.
None of these values is less than or equal to k = 1, so the answer is -1.
Example 3:

Input: nums = [0], k = 0

Output: 0

Explanation:

At index 0, the instability score is 0 - 0 = 0, which is less than or equal to k = 0. Therefore, the answer is 0.

 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
0 <= k <= 109
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
47,147/68.6K
Acceptance Rate
68.7%
Topics
Mid Level
Array
Prefix Sum
Weekly Contest 498
icon
Companies
Hint 1
Simulate as described
''')
