from lc import *

# https://leetcode.com/problems/stone-game-iii/discuss/1387328/Pytohn-DP-Recursive-and-iterative-O(1)-Space-Explained

class Solution:
    def stoneGameIII(self, v: List[int]) -> str:
        o=[0,0,0];any(setitem(o,i%3,max(sum(v[i:i+k])-o[(i+k)%3]for k in range(1,4)))for i in range(len(v)-1,-1,-1));return(('Bob','Tie')[o[0]==0],'Alice')[o[0]>0]

class Solution:
    def stoneGameIII(self, v: List[int]) -> str:
        f=cache(lambda i:i<len(v)and max(sum(v[i:i+k])-f(i+k)for k in range(1,4)));r=f(0);return('Bob','Tie','Alice')[(r>0)-(r<0)+1]

class Solution:
    def stoneGameIII(self, v: List[int]) -> str:
        f=cache(lambda i:i<len(v)and max(sum(v[i:i+k])-f(i+k)for k in range(1,4)));r=f(0);return(('Bob','Tie')[r==0],'Alice')[r>0]

class Solution:
    def stoneGameIII(self, v: List[int]) -> str:
        f=cache(lambda i:i<len(v)and max(sum(v[i:i+k])-f(i+k)for k in(1,2,3)));r=f(0);return(('Bob','Tie')[r==0],'Alice')[r>0]

class Solution:
    def stoneGameIII(self, v: List[int]) -> str:
        f=cache(lambda i:i<len(v)and max(sum(v[i:i+k])-f(i+k)for k in(1,2,3)));return(('Bob','Tie')[f(0)==0],'Alice')[f(0)>0]

class Solution:
    def stoneGameIII(self, v: List[int]) -> str:
        f=cache(lambda i:i<len(v)and max(sum(v[i:i+k])-f(i+k)for k in(1,2,3)));return('Bob','Alice')[f(0)>0]if f(0)else'Tie'

test('''
1406. Stone Game III
Hard

1461

38

Add to List

Share
Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2, or 3 stones from the first remaining stones in the row.

The score of each player is the sum of the values of the stones taken. The score of each player is 0 initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob play optimally.

Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with the same score.

 

Example 1:

Input: values = [1,2,3,7]
Output: "Bob"
Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.
Example 2:

Input: values = [1,2,3,-9]
Output: "Alice"
Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. In the next move, Alice will take the pile with value = -9 and lose.
If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. In the next move, Alice will take the pile with value = -9 and also lose.
Remember that both play optimally so here Alice will choose the scenario that makes her win.
Example 3:

Input: values = [1,2,3,6]
Output: "Tie"
Explanation: Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.
 

Constraints:

1 <= stoneValue.length <= 5 * 104
-1000 <= stoneValue[i] <= 1000
Accepted
51,595
Submissions
84,317
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
The game can be mapped to minmax game. Alice tries to maximize the total score and Bob tries to minimize it.
Use dynamic programming to simulate the game. If the total score was 0 the game is "Tie", and if it has positive value then "Alice" wins, otherwise "Bob" wins.
''')

