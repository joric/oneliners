from lc import *

# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/solutions/6173955/one-line-method/?envType=daily-question&envId=2025-10-18

# const maxDistinctElements = (nums, k, m = -Infinity, l = nums.sort((x, y) => x - y)) => l.length - l.reduce((s, v) => v + k <= m ? s + 1 : (m = Math.max(m + 1, v - k), s), 0);

class Solution:
    def maxDistinctElements(self, a: List[int], k: int) -> int:
        m=-inf;return len(a)-sum((m:=[max(m+1,x-k),m][x+k<=m])and x+k<=m for x in sorted(a))

# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/solutions/6393698/python-simple-greedy-o-n-log-n-solution-10-lines-of-code/?envType=daily-question&envId=2025-10-18

class Solution:
    def maxDistinctElements(self, a: List[int], k: int) -> int:
        a.sort()
        r = 0
        p=-inf
        for x in a:
            n = min(max(p+1,x-k),x+k)
            r += n > p
            p = n
        return r

class Solution:
    def maxDistinctElements(self, a: List[int], k: int) -> int:
        p=-inf;return sum((n:=min(max(p+1,x-k),x+k))>p+n-(p:=n)for x in sorted(a))

test('''
3397. Maximum Number of Distinct Elements After Operations
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and an integer k.

You are allowed to perform the following operation on each element of the array at most once:

Add an integer in the range [-k, k] to the element.
Return the maximum possible number of distinct elements in nums after performing the operations.

 

Example 1:

Input: nums = [1,2,2,3,3,4], k = 2

Output: 6

Explanation:

nums changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.

Example 2:

Input: nums = [4,4,4,4], k = 1

Output: 3

Explanation:

By adding -1 to nums[0] and 1 to nums[1], nums changes to [3, 5, 4, 4].

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= k <= 109
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
36,551/91K
Acceptance Rate
40.2%
Topics
Array
Greedy
Sorting
Weekly Contest 429
icon
Companies
Hint 1
Can we use sorting here?
Hint 2
Find the minimum element which is not used for each element.
Similar Questions
Least Number of Unique Integers after K Removals
Medium
''')
