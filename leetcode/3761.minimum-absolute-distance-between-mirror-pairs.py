from lc import *

# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/solutions/7926397/minimum-absolute-distance-between-mirror-oc90/?envType=daily-question&envId=2026-04-17

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        prev = dict()
        ans = inf
        for i, num in enumerate(nums):
            if num in prev:
                ans = min(ans, i - prev[num])
            prev[int(str(num)[::-1])] = i
        return -1 if ans == inf else ans

class Solution:
    def minMirrorPairDistance(self, a: List[int]) -> int:
        d={};return(-1,t:=min((i-d.get(x,-inf),d.update({int(str(x)[::-1]):i}))[0]for i,x in enumerate(a)))[t<inf]

test('''
3761. Minimum Absolute Distance Between Mirror Pairs
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

A mirror pair is a pair of indices (i, j) such that:

0 <= i < j < nums.length, and
reverse(nums[i]) == nums[j], where reverse(x) denotes the integer formed by reversing the digits of x. Leading zeros are omitted after reversing, for example reverse(120) = 21.
Return the minimum absolute distance between the indices of any mirror pair. The absolute distance between indices i and j is abs(i - j).

If no mirror pair exists, return -1.

 

Example 1:

Input: nums = [12,21,45,33,54]

Output: 1

Explanation:

The mirror pairs are:

(0, 1) since reverse(nums[0]) = reverse(12) = 21 = nums[1], giving an absolute distance abs(0 - 1) = 1.
(2, 4) since reverse(nums[2]) = reverse(45) = 54 = nums[4], giving an absolute distance abs(2 - 4) = 2.
The minimum absolute distance among all pairs is 1.

Example 2:

Input: nums = [120,21]

Output: 1

Explanation:

There is only one mirror pair (0, 1) since reverse(nums[0]) = reverse(120) = 21 = nums[1].

The minimum absolute distance is 1.

Example 3:

Input: nums = [21,120]

Output: -1

Explanation:

There are no mirror pairs in the array.

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109​​​​​​​
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
22,420/50.4K
Acceptance Rate
44.5%
Topics
Staff
Array
Hash Table
Math
Weekly Contest 478
icon
Companies
Hint 1
Scan left to right with a hash map: for each nums[i], if the map contains key nums[i] then set ans = min(ans, i - map[nums[i]]).
Hint 2
Store/update the current index under key reverse(nums[i]), so future matches use the most recent index.
''')
