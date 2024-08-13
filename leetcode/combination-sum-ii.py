from lc import *

# https://leetcode.com/problems/combination-sum-ii/discuss/670707/Python-in-6-lines

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.recurse(sorted(candidates), target)
    def recurse(self, cans, t):
        if not cans or cans[0] > t: return []
        if cans[0] == t: return [[t]]
        i = len(list(itertools.takewhile(lambda x: x==cans[0], cans)))
        return [[cans[0]] + sol for sol in self.recurse(cans[1:], t-cans[0])] + self.recurse(cans[i:], t)

class Solution:
    def combinationSum2(self, c: List[int], t: int) -> List[List[int]]:
        def f(c,t):
            if not c or c[0] > t:
                return []
            if c[0] == t:
                return [[t]]
            return [[c[0]]+x for x in f(c[1:], t-c[0])] + f(c[sum(x==c[0]for x in c):], t)
        return f(sorted(c),t)

class Solution:
    def combinationSum2(self, c: List[int], t: int) -> List[List[int]]:
        return(f:=lambda c,t:c and(t==c[0]and[[t]]or t>c[0]and[[c[0]]+x for x in f(c[1:],t-c[0])]+f(c[sum(x==c[0]for x in c):],t)or[]))(sorted(c),t)

test('''
40. Combination Sum II
Medium

10551

302

Add to List

Share
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
Accepted
1,045,066
Submissions
1,899,049
''')
