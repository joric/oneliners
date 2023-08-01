from lc import *

# https://leetcode.com/problems/combinations/discuss/27024/1-liner-3-liner-4-liner

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        return [pre+[i] for i in range(k,n+1) for pre in self.combine(i-1, k-1)]

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = [[]]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
        return combs

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return reduce(lambda C,_:[[i]+c for c in C for i in range(1, c[0] if c else n+1)],range(k),[[]])

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations(range(1,n+1),k)

test('''
77. Combinations
Medium

6347

192

Add to List

Share
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 

Constraints:

1 <= n <= 20
1 <= k <= n
''')

