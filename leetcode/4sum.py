from lc import *

def check(res, expected, nums, target):
    return (u:=lambda v: sorted(list(map(sorted,v))))(res)==u(expected)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res,c,d = set(), Counter(nums), defaultdict(set)

        for a,b in combinations(nums, 2):
            d[a+b].add((a,b))

        for v in d:
            if target-v in d:
                for p1 in d[v]:
                    for p2 in d[target-v]:
                        p = sorted(p1+p2)
                        if tuple(p) not in res and all(p.count(n)<=c[n] for n in p):
                            res.add(tuple(p))
        return [list(p) for p in res]

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
