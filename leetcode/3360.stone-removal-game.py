from lc import *

# https://leetcode.com/problems/stone-removal-game/solutions/6076502/python-one-line-by-ante-w9w4/?envType=daily-question&envId=2026-11-26

class Solution:
    def canAliceWin(self, n, last = 11):
        return False if n < last - 1 else not self.canAliceWin(n - last + 1, last - 1)

# https://leetcode.com/problems/stone-removal-game/solutions/6075823/simple-one-line-by-silvia42-z9f4/?envType=daily-question&envId=2026-11-26

class Solution:
    def canAliceWin(self, n: int) -> bool:
        return 9<n<19 or 26<n<34 or 39<n<45 or 48<n<52

# cpp version return !!((int)ceil((sqrt(441 - 8 * n) - 1) / 2) % 2);

# https://leetcode.com/problems/stone-removal-game/solutions/6079742/one-line-math-o1-by-xxxxkav-a64a/?envType=daily-question&envId=2026-11-26

class Solution:
    def canAliceWin(self, n: int) -> bool:
        return ((21 - sqrt(21*21 - 8*n))//2) % 2 == 1

class Solution:
    def canAliceWin(self, n: int) -> bool:
        return((21-sqrt(441-8*n))//2)%2==1

class Solution:
    def canAliceWin(self, n: int) -> bool:
        return 0<1<<n&0x61f03f807fc00

# https://leetcode.com/problems/stone-removal-game/solutions/8624873/stone-cold-math-closed-form-o1-by-asnork-lq22/?envType=daily-question&envId=2026-11-26

class Solution:
    def canAliceWin(self, n: int) -> bool:
        return round(sqrt(110-2*n))%2==1

class Solution:
    def canAliceWin(self, n: int) -> bool:
        return 1<(440-8*n)**.5%4<3

class Solution:
    def canAliceWin(self, n: int) -> bool:
        return(440-8*n)**.5%4%3>1

class Solution:
    def canAliceWin(self, n: int) -> bool:
        return(57-n)**.4%.78>.4

test('''
3360. Stone Removal Game
Easy
Topics
premium lock icon
Companies
Hint
Alice and Bob are playing a game where they take turns removing stones from a pile, with Alice going first.

Alice starts by removing exactly 10 stones on her first turn.
For each subsequent turn, each player removes exactly 1 fewer stone than the previous opponent.
The player who cannot make a move loses the game.

Given a positive integer n, return true if Alice wins the game and false otherwise.

 

Example 1:

Input: n = 12

Output: true

Explanation:

Alice removes 10 stones on her first turn, leaving 2 stones for Bob.
Bob cannot remove 9 stones, so Alice wins.
Example 2:

Input: n = 1

Output: false

Explanation:

Alice cannot remove 10 stones, so Alice loses.
 

Constraints:

1 <= n <= 50
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
38,259/88.6K
Acceptance Rate
43.2%
Topics
Mid Level
Math
Simulation
Biweekly Contest 144
icon
Companies
Hint 1
The constraints are small enough that a brute-force solution is feasible.
Similar Questions
Stone Game IV
Hard
''')
