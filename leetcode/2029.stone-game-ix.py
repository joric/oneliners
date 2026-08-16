from lc import *

# https://leetcode.com/problems/stone-game-ix/solutions/1500214/4-line-java-solution-by-binglelove-wcrq/?envType=daily-question&envId=2026-08-16

class Solution:
    def stoneGameIX(self, s: List[int]) -> bool:
        c = [0,0,0]
        for x in s: c[x%3] += 1
        return not ((c[0]%2==0 and (c[1]==0 or c[2]==0)) or (c[0]%2==1 and abs(c[1]-c[2])<3))

class Solution:
    def stoneGameIX(self,s:List[int])->bool:
        c=Counter(x%3 for x in s);return c[0]%2 and abs(c[1]-c[2])>=3 or c[0]%2==0<c[1]*c[2]

class Solution:
    def stoneGameIX(self, s: List[int]) -> bool:
        c=Counter(x%3 for x in s);return[c[1]*c[2]>0,abs(c[1]-c[2])>2][c[0]%2]

test('''
2029. Stone Game IX
Medium
Topics
premium lock icon
Companies
Hint
Alice and Bob continue their games with stones. There is a row of n stones, and each stone has an associated value. You are given an integer array stones, where stones[i] is the value of the ith stone.

Alice and Bob take turns, with Alice starting first. On each turn, the player may remove any stone from stones. The player who removes a stone loses if the sum of the values of all removed stones is divisible by 3. Bob will win automatically if there are no remaining stones (even if it is Alice's turn).

Assuming both players play optimally, return true if Alice wins and false if Bob wins.

 

Example 1:

Input: stones = [2,1]
Output: true
Explanation: The game will be played as follows:
- Turn 1: Alice can remove either stone.
- Turn 2: Bob removes the remaining stone. 
The sum of the removed stones is 1 + 2 = 3 and is divisible by 3. Therefore, Bob loses and Alice wins the game.
Example 2:

Input: stones = [2]
Output: false
Explanation: Alice will remove the only stone, and the sum of the values on the removed stones is 2. 
Since all the stones are removed and the sum of values is not divisible by 3, Bob wins the game.
Example 3:

Input: stones = [5,1,2,4,3]
Output: false
Explanation: Bob will always win. One possible way for Bob to win is shown below:
- Turn 1: Alice can remove the second stone with value 1. Sum of removed stones = 1.
- Turn 2: Bob removes the fifth stone with value 3. Sum of removed stones = 1 + 3 = 4.
- Turn 3: Alices removes the fourth stone with value 4. Sum of removed stones = 1 + 3 + 4 = 8.
- Turn 4: Bob removes the third stone with value 2. Sum of removed stones = 1 + 3 + 4 + 2 = 10.
- Turn 5: Alice removes the first stone with value 5. Sum of removed stones = 1 + 3 + 4 + 2 + 5 = 15.
Alice loses the game because the sum of the removed stones (15) is divisible by 3. Bob wins the game.
 

Constraints:

1 <= stones.length <= 105
1 <= stones[i] <= 104
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
12,745/41.2K
Acceptance Rate
31.0%
Topics
icon
Companies
Hint 1
There are limited outcomes given the current sum and the stones remaining.
Hint 2
Can we greedily simulate starting with taking a stone with remainder 1 or 2 divided by 3?
Similar Questions
Stone Game
Medium
Stone Game II
Medium
Stone Game III
Hard
Stone Game IV
Hard
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
''')
