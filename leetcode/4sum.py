from lc import *

def check(res, expected, nums, target):
    return (u:=lambda v: sorted(list(map(sorted,v))))(res)==u(expected)

class Solution:
    def fourSum(self, v: List[int], target: int) -> List[List[int]]:
        v.sort()
        n, r = len(v), []
        for i in range(n):
            for j in range(i + 1, n):
                d = target - v[i] - v[j]
                a, b = j + 1, n - 1
                while a < b:
                    if v[a] + v[b] < d:
                        a += 1
                    elif v[a] + v[b] > d:
                        b -= 1
                    else:
                        r.append((v[i], v[j], v[a], v[b]))
                        a += 1
                        b -= 1
        return set(r)


test('''

18. 4Sum
Medium

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:

1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9

''', check=check)
