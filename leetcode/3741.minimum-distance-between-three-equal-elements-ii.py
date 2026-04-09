from lc import *

# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/solutions/7337834/python3-one-pass-ts-366-ms-48-mb-by-spau-v4gk/

class Solution:
    def minimumDistance(self, a: List[int]) -> int:
        d = defaultdict(list)
        r = inf
        for i,j in enumerate(a):
            d[j].append(i)
            if len(d[j])<3:
                continue
            r = min(r,d[j][-1]-d[j][-3])
        return -1 if r == inf else r+r

class Solution:
    def minimumDistance(self, a: List[int]) -> int:
        d=defaultdict(list);t=min((d[j][-1]-d[j][-3]for i,j in enumerate(a)if d[j].append(i)or len(d[j])>2),default=inf);return t<inf and t+t or-1

test('''
3741. Minimum Distance Between Three Equal Elements II
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].

The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.

Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.

 

Example 1:

Input: nums = [1,2,1,1,3]

Output: 6

Explanation:

The minimum distance is achieved by the good tuple (0, 2, 3).

(0, 2, 3) is a good tuple because nums[0] == nums[2] == nums[3] == 1. Its distance is abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6.

Example 2:

Input: nums = [1,1,2,3,2,1,2]

Output: 8

Explanation:

The minimum distance is achieved by the good tuple (2, 4, 6).

(2, 4, 6) is a good tuple because nums[2] == nums[4] == nums[6] == 2. Its distance is abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8.

Example 3:

Input: nums = [1]

Output: -1

Explanation:

There are no good tuples. Therefore, the answer is -1.

 

Constraints:

1 <= n == nums.length <= 105
1 <= nums[i] <= n
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
30,853/47.3K
Acceptance Rate
65.3%
Topics
Senior
Array
Hash Table
Weekly Contest 475
icon
Companies
Hint 1
The distance formula abs(i - j) + abs(j - k) + abs(k - i) simplifies to 2 * (max(i, j, k) - min(i, j, k)).
Hint 2
Group the indices for each unique number. For a number to form a good tuple, it must appear at least 3 times.
Hint 3
For each number that appears at least 3 times, we want to find three of its indices p < q < r that minimize r - p. This is achieved by considering every three consecutive indices in the sorted list of indices.
''')
