from lc import *

# https://leetcode.com/problems/stone-game-v/solutions/8439372/avoid-tle-with-branch-pruning-by-grumpyg-4i98/?envType=daily-question&envId=2026-08-17

class Solution:
    def stoneGameV(self, s: List[int]) -> int:
        n = len(s)
        a = [0,*accumulate(s)]
        @cache
        def f(i, j): 
            if i == j:
                return 0 
            best = -inf
            for p in range(i, j): 
                left = a[p + 1] - a[i]
                right = a[j + 1] - a[p + 1]
                if 2 * min(left, right) < best:
                    break
                if left <= right:
                    best = max(best, left + f(i, p)) 
                if right <= left:
                    best = max(best, right + f(p + 1, j))  
            return best
        return f(0, n - 1)

class Solution:
    def stoneGameV(self, s: List[int]) -> int:
        a=[0,*accumulate(s)]
        @cache
        def f(i,j):
            if i==j:return 0
            b=-inf
            for p in range(i,j):
                l,r=a[p+1]-a[i],a[j+1]-a[p+1]
                if 2*min(l,r)<b:break
                if l<=r:b=max(b,l+f(i,p))
                if r<=l:b=max(b,r+f(p+1,j))
            return b
        return f(0,len(s)-1)

class Solution:
    def stoneGameV(self,s:List[int])->int:
        a=[0,*accumulate(s)]
        @cache
        def f(i,j):
            if i==j:return 0
            b=-inf
            next((1 for p in range(i,j) for l,r in[(a[p+1]-a[i],a[j+1]-a[p+1])] if 2*min(l,r)<b or((b:=max(b,l+f(i,p) if l<=r else-inf,r+f(p+1,j) if r<=l else-inf))and False)),0)
            return b
        return f(0,len(s)-1)

class Solution:
    def stoneGameV(self,s:List[int])->int:
        a=[0,*accumulate(s)];f=cache(lambda i,j:0 if i==j else[(b:=[-inf]),next((1 for p in range(i,j)for l,r in[(a[p+1]-a[i],a[j+1]-a[p+1])]if 2*min(l,r)<b[0]or setitem(b,0,max(b[0],(l+f(i,p))if l<=r else-inf,(r+f(p+1,j))if r<=l else-inf))or 0),0)][0][0]);return f(0,len(s)-1)

test('''
1563. Stone Game V
Hard
Topics
premium lock icon
Companies
Hint
There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only one stone remaining. Alice's score is initially zero.

Return the maximum score that Alice can obtain.

 

Example 1:

Input: stoneValue = [6,2,3,4,5,5]
Output: 18
Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.
Example 2:

Input: stoneValue = [7,7,7,7,7,7,7]
Output: 28
Example 3:

Input: stoneValue = [4]
Output: 0

Other examples:

Input: stoneValue = [2,1,1]
Output: 3

Input: stoneValue = [4]
Output: 0

Constraints:

1 <= stoneValue.length <= 500
1 <= stoneValue[i] <= 106
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
29,417/68.4K
Acceptance Rate
43.0%
Topics
Principal
Array
Math
Dynamic Programming
Game Theory
Weekly Contest 203
icon
Companies
Hint 1
We need to try all possible divisions for the current row to get the max score.
Hint 2
As calculating all possible divisions will lead us to calculate some sub-problems more than once, we need to think of dynamic programming.
Similar Questions
Stone Game
Medium
Stone Game II
Medium
Stone Game III
Hard
Stone Game IV
Hard
Stone Game VI
Medium
Stone Game VII
Medium
Stone Game VIII
Hard
Stone Game IX
Medium
''')
