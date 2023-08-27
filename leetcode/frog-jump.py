from lc import *

# https://leetcode.com/problems/frog-jump/discuss/583442/The-only-one-true-simply-DP-solution

class Solution:
    def canCross(self, s: List[int]) -> bool:
        n = len(s)
        d = [[False]*n for _ in s]
        d[0][1] = True
        for i in range(1,n):
            for j in range(i):
                k = s[i] - s[j]
                if k>0 and k<n and d[j][k]:
                    if i==n-1:
                        return True;
                    d[i][k] = True
                    if k-1>=0:
                        d[i][k-1] = True
                    if k+1<=n:
                        d[i][k+1] = True
        return False

# https://leetcode.com/problems/frog-jump/discuss/1097146/python-dfs-%2B-cache

class Solution:
    def canCross(self, s: List[int]) -> bool:
        @cache
        def f(i,u):
            if i == s[-1]:
                return True
            if i not in s:
                return False
            for v in range(u-1,u+2):
                if v == 0:
                    continue
                if f(i+v,v):
                    return True
            return False
        return f(1,1)

class Solution:
    def canCross(self, s: List[int]) -> bool:
        return(f:=cache(lambda i,u:i==s[-1]or i in s and any(v and f(i+v,v)for v in range(u-1,u+2))))(1,1)

class Solution:
    def canCross(self, s: List[int]) -> bool:
        return(f:=cache(lambda i,u:i==s[-1]or any(v and f(i+v,v)for v in range(u-1,u+2)if i in s)))(1,1)

test('''
403. Frog Jump
Hard

4255

204

Add to List

Share
A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.

 

Example 1:

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
 

Constraints:

2 <= stones.length <= 2000
0 <= stones[i] <= 2^31 - 1
stones[0] == 0
stones is sorted in a strictly increasing order.
''')

