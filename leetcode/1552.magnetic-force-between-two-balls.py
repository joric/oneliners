from lc import *

# https://leetcode.com/problems/magnetic-force-between-two-balls/discuss/1128568/Python-3-binary-search-fast

class Solution:
    def maxDistance(self, p: List[int], m: int) -> int:
        p.sort()
        def f(k):
            i = n = 0
            while i<len(p):
                i = bisect_left(p,p[i]+k+1)
                n += 1
            return n < m
        return bisect_left(range(max(p)),1,key=f)

class Solution:
    def maxDistance(self, p: List[int], m: int) -> int:
        p.sort();return bisect_left(range(max(p)),1,key=lambda k:(i:=0)or sum(i<len(p)and(i:=bisect_right(p,p[i]+k),1)[1]for _ in p)<m)

# https://leetcode.com/problems/magnetic-force-between-two-balls/discuss/5339506/Python-bisect_left

class Solution:
    def maxDistance(self, p: List[int], m: int) -> int:
        p.sort()
        def f(d):
            n,x = 1,p[0]
            for y in p:
                if y - x > d:
                    x = y
                    n += 1
            return n<m
        return bisect_left(range(max(p)),1,key=lambda d:f(d))

class Solution:
    def maxDistance(self, p: List[int], m: int) -> int:
        p.sort();return bisect_left(range(max(p)),1,key=lambda d:[x:=p[0]]and-~sum(y-x>d and[x:=y]!=0 for y in p)<m)

class Solution:
    def maxDistance(self, p: List[int], m: int) -> int:
        return bisect_left(range(10**9),1,key=lambda d:[x:=-d]and sum(y-x>d and(x:=y)>0 for y in sorted(p))<m)

test('''
1552. Magnetic Force Between Two Balls
Medium

2273

149

Add to List

Share
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

 

Example 1:


Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
Example 2:

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.
 

Constraints:

n == position.length
2 <= n <= 105
1 <= position[i] <= 109
All integers in position are distinct.
2 <= m <= position.length
Accepted
75,688
Submissions
116,493
''')