from lc import *

# https://leetcode.com/problems/count-special-triplets/solutions/6844768/javacpython-two-passes-by-lee215-vot5/?envType=daily-question&envId=2025-12-09

class Solution:
    def specialTriplets(self, a: List[int]) -> int:
        l,r=Counter(),Counter(a);return sum((r.update({x:-1}),l[x*2]*r[x*2],l.update([x]))[1]for x in a)%(10**9+7)

# https://leetcode.com/problems/count-special-triplets/description/?envType=daily-question&envId=2025-12-09

class Solution:
    def specialTriplets(self, a: List[int]) -> int:
        f=lambda a,z:[(z[v*2],z.update([v]))[0] for v in a];return sum(map(mul,f(a,Counter()),f(a[::-1],Counter())[::-1]))%(10**9+7)

class Solution:
    def specialTriplets(self, a: List[int]) -> int:
        z1,z2=Counter(),Counter(); return sum((z2[v/2],z2.update({v:z1[v*2]}),z1.update([v]))[0]for v in a)%(10**9+7)

class Solution:
    def specialTriplets(self, a: List[int]) -> int:
        f=lambda a,z:[(z[v*2],z.update([v]))[0]for v in a];return sum(map(mul,f(a,Counter()),f(a[::-1],Counter())[::-1]))%(10**9+7)

class Solution:
    def specialTriplets(self, a: List[int]) -> int:
        l,r=Counter(),Counter();return sum((r[x/2],r.update({x:l[x*2]}),l.update([x]))[0]for x in a)%(10**9+7)

test('''
3583. Count Special Triplets
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

A special triplet is defined as a triplet of indices (i, j, k) such that:

0 <= i < j < k < n, where n = nums.length
nums[i] == nums[j] * 2
nums[k] == nums[j] * 2
Return the total number of special triplets in the array.

Since the answer may be large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [6,3,6]

Output: 1

Explanation:

The only special triplet is (i, j, k) = (0, 1, 2), where:

nums[0] = 6, nums[1] = 3, nums[2] = 6
nums[0] = nums[1] * 2 = 3 * 2 = 6
nums[2] = nums[1] * 2 = 3 * 2 = 6
Example 2:

Input: nums = [0,1,0,0]

Output: 1

Explanation:

The only special triplet is (i, j, k) = (0, 2, 3), where:

nums[0] = 0, nums[2] = 0, nums[3] = 0
nums[0] = nums[2] * 2 = 0 * 2 = 0
nums[3] = nums[2] * 2 = 0 * 2 = 0
Example 3:

Input: nums = [8,4,2,8,4]

Output: 2

Explanation:

There are exactly two special triplets:

(i, j, k) = (0, 1, 3)
nums[0] = 8, nums[1] = 4, nums[3] = 8
nums[0] = nums[1] * 2 = 4 * 2 = 8
nums[3] = nums[1] * 2 = 4 * 2 = 8
(i, j, k) = (1, 2, 4)
nums[1] = 4, nums[2] = 2, nums[4] = 4
nums[1] = nums[2] * 2 = 2 * 2 = 4
nums[4] = nums[2] * 2 = 2 * 2 = 4
 

Constraints:

3 <= n == nums.length <= 105
0 <= nums[i] <= 105
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
27,373/73.2K
Acceptance Rate
37.4%
Topics
Array
Hash Table
Counting
Weekly Contest 454
icon
Companies
Hint 1
Use frequency arrays or maps, e.g. freqPrev and freqNext—to track how many times each value appears before and after the current index.
Hint 2
For each index j in the triplet (i,j,k), compute its contribution to the answer using your freqPrev and freqNext counts.
''')
