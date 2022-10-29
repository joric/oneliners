from lc import *

def check(res, expected, nums, target):
    return sorted(res)==sorted(expected)

# TLE https://leetcode.com/problems/4sum/discuss/8595/5-lines-simple-Python
class Solution1:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums, dic = sorted(nums), collections.defaultdict(list)
        for (i, a), (j, b) in itertools.combinations(enumerate(nums), 2):
            dic[a+b].append([i, j])

        res = set(tuple(sorted(nums[i] for i in (head + tail))) for ab in dic \
              if target - ab in dic for head in dic[ab] for tail in dic[target-ab] \
              if len(set(head + tail)) == 4)
        return list(map(list, res))

class Solution2:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        r,c,d = set(), Counter(nums), defaultdict(set)
        for a,b in combinations(nums, 2):
            d[a+b].add((a,b))
        for v in d:
            if target-v in d:
                for p1 in d[v]:
                    for p2 in d[target-v]:
                        p = tuple(sorted(p1+p2))
                        if p not in r and all(p.count(n)<=c[n] for n in p):
                            r.add(p)
        return r

class Solution3:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        c = Counter(nums)
        d = reduce(lambda d,t:d[sum(t)].add(t) or d, combinations(nums, 2), defaultdict(set))
        k = lambda r,p: (p not in r and all(p.count(n)<=c[n] for n in p)) and r.add(p) or r
        f = lambda r,v: reduce(k, (tuple(sorted(a+b)) for a in d[v] for b in d[target-v]), r)
        return reduce(f, (v for v in d if target-v in d), set())

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return (c:=Counter(nums),d:=reduce(lambda d,t: d[sum(t)].add(t) or d, combinations(nums, 2),
            defaultdict(set))) and reduce(lambda r,v: reduce(lambda r,p: (p not in r and all(p.count(n)<=c[n] for n in p))
            and r.add(p) or r, (tuple(sorted(a+b)) for a in d[v] for b in d[target-v]), r), (v for v in d if target-v in d),set())

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
