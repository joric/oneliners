from lc import *

# https://leetcode.com/problems/count-number-of-bad-pairs/solutions/5630520/one-line-solution/?envType=daily-question&envId=2025-02-09

class Solution:
    def countBadPairs(self, a: List[int]) -> int:
        return comb(len(x),2)-sum(comb(x,2) for x in Counter(starmap(sub,enumerate(a))).values())

class Solution:
    def countBadPairs(self, a: List[int]) -> int:
        return sum(x*(len(a)-x)for x in Counter(starmap(sub,enumerate(a))).values())//2

class Solution:
    def countBadPairs(self, a: List[int]) -> int:
        return sum(x*(len(a)-x)for x in Counter(map(sub,a,count())).values())//2

test('''
2364. Count Number of Bad Pairs
Medium
Topics
Companies
Hint
You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.

 

Example 1:

Input: nums = [4,1,3,3]
Output: 5
Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.
Example 2:

Input: nums = [1,2,3,4,5]
Output: 0
Explanation: There are no bad pairs.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
Seen this question in a real interview before?
1/5
Yes
No
Accepted
41.7K
Submissions
94.7K
Acceptance Rate
44.1%
Topics
Array
Hash Table
Math
Counting
Companies
Hint 1
Would it be easier to count the number of pairs that are not bad pairs?
Hint 2
Notice that (j - i != nums[j] - nums[i]) is the same as (nums[i] - i != nums[j] - j).
Hint 3
Keep a counter of nums[i] - i. To be efficient, use a HashMap.
Similar Questions
K-diff Pairs in an Array
Medium
Subarray Sums Divisible by K
Medium
Count Nice Pairs in an Array
Medium
Count Number of Pairs With Absolute Difference K
Easy
Count Equal and Divisible Pairs in an Array
Easy
Number of Pairs Satisfying Inequality
Hard
''')
