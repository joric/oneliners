from lc import *

# https://leetcode.com/problems/stone-game-ii

class Solution:
    def stoneGameII(self, p: List[int]) -> int:
        return(f:=cache(lambda i,m:max([sum(p[i:])-f(j,max(m,j-i))for j in range(i+1,min(2*m+i+1,len(p)+1))]+[0])))(0,1)

test('''
1140. Stone Game II
Medium

1957

402

Add to List

Share
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

 

Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
Example 2:

Input: piles = [1,2,3,4,5,100]
Output: 104
 

Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 104
Accepted
56,459
Submissions
84,994
Seen this question in a real interview before?

Yes

No
Stone Game V
Hard
Stone Game VI
Medium
Stone Game VII
Medium
Stone Game VIII
Hard
Stone Game IX
Medium
Use dynamic programming: the states are (i, m) for the answer of piles[i:] and that given m.
''')