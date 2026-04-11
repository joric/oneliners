from lc import *

# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/solutions/7508420/on-python-beats-100-one-pass-with-dictio-mm7j/?envType=daily-question&envId=2026-04-10

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        seen = dict()
        result, not_found = len(nums), -len(nums)
        for k, x in enumerate(nums):
            j = not_found
            if x in seen:
                i, j = seen[x]
                result = min(result, k - i)
            seen[x] = (j, k)
        return -1 if result >= len(nums) else 2 * result

# same as 3741

class Solution:
    def minimumDistance(self, a: List[int]) -> int:
        d=defaultdict(list);t=min((d[j][-1]-d[j][-3]for i,j in enumerate(a)if d[j].append(i)or len(d[j])>2),default=-1);return(t>0)*(t*2+1)-1

test('''
3740. Minimum Distance Between Three Equal Elements I
Easy
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

1 <= n == nums.length <= 100
1 <= nums[i] <= n
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
38,491/63.5K
Acceptance Rate
60.6%
Topics
Mid Level
Array
Hash Table
Weekly Contest 475
icon
Companies
Hint 1
Use bruteforce
''')
