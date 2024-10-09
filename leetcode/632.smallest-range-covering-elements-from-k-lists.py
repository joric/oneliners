from lc import *

# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/discuss/5493444/Only-9-lines-Simple-With-Explanation

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        avls = sorted(set(sum(nums, [])))
        mx = min(nums, key=itemgetter(-1))[-1]
        avls = avls[:bisect_right(avls, mx)]
        ans = [0, math.inf]
        for l in avls:
            r = max([lst[bisect_left(lst, l)] for lst in nums])
            if r - l < ans[1] - ans[0]:
                ans = [l, r]
        return ans

class Solution:
    def smallestRange(self, a: List[List[int]]) -> List[int]:
        b=sorted({*sum(a,[])});b=b[:bisect_right(b,min(a,key=itemgetter(-1))[-1])];q=[0,inf];[(r:=max([t[bisect_left(t,l)]for t in a]))-l<q[1]-q[0] and(q:=[l,r])for l in b];return q

test('''
632. Smallest Range Covering Elements from K Lists
Hard

3505

77

Add to List

Share
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

 

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]
 

Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] is sorted in non-decreasing order.
Accepted
116,325
Submissions
183,424
''')
