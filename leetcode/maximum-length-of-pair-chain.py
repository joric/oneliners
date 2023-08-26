from lc import *

# https://leetcode.com/problems/maximum-length-of-pair-chain/discuss/105607/4-Liner-Python-Greedy

class Solution:
    def findLongestChain(self, p: List[List[int]]) -> int:
        c,r=-inf,0
        for x in sorted(p,key=itemgetter(1)):
            if c < x[0]:
                c = x[1]
                r += 1
        return r

class Solution:
    def findLongestChain(self, p: List[List[int]]) -> int:
        c,r=-inf,0;[c<x[0]and(c:=x[1],r:=r+1)for x in sorted(p,key=itemgetter(1))];return r

test('''
646. Maximum Length of Pair Chain
Medium

3308

118

Add to List

Share
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.

 

Example 1:

Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].
Example 2:

Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
 

Constraints:

n == pairs.length
1 <= n <= 1000
-1000 <= lefti < righti <= 1000
''')

