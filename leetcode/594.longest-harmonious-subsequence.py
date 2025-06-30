from lc import *

# https://leetcode.com/problems/longest-harmonious-subsequence/solutions/103517/python-3-line/

class Solution:
    def findLHS(self, a: List[int]) -> int:
        c=Counter(a);t=sorted(c.keys());return max([0]+[c[x]+c[y]for x,y in zip(t[0:],t[1:])if y-x==1])

# https://leetcode.com/problems/longest-harmonious-subsequence/solutions/4264818/easy-6-lines-python-solution-97/

class Solution:
    def findLHS(self, a: List[int]) -> int:
        c=Counter(a);return max([0]+[c[k]+c[k+1]for k in c if k+1 in c])

# https://leetcode.com/problems/longest-harmonious-subsequence/solutions/4070395/python-3-use-counter-with-2-lines/

class Solution:
    def findLHS(self, a: list[int]) -> int:
        c=Counter(a);return max((0,c[k]+c[k+1])[k+1in c]for k in c)

class Solution:
    def findLHS(self, a: list[int]) -> int:
        c=Counter(a);return max((c[k]+c[k+1])*(k+1in c)for k in c)

test('''
594. Longest Harmonious Subsequence
Solved
Easy
Topics
premium lock icon
Companies
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

 

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]

Output: 5

Explanation:

The longest harmonious subsequence is [3,2,2,2,3].

Example 2:

Input: nums = [1,2,3,4]

Output: 2

Explanation:

The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

Example 3:

Input: nums = [1,1,1,1]

Output: 0

Explanation:

No harmonic subsequence exists.

Other examples:

Input: nums = [1,3,5,7,9,11,13,15,17]
Output: 0

Constraints:

1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109
Seen this question in a real interview before?
1/5
Yes
No
Accepted
215,300/371K
Acceptance Rate
58.0%
Topics
Array
Hash Table
Sliding Window
Sorting
Counting
''')
