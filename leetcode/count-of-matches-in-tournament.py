from lc import *

sys.setrecursionlimit(10**6) 

class Solution:
    def numberOfMatches(self, n: int) -> int:
        self.ans = 0
        def helper(n):
            if n<=1:
                return
            if n%2==0:
                self.ans+=(n//2)
                helper(n//2)
            else:
                self.ans+=n//2
                helper(1+n//2)
        helper(n)
        return self.ans

class Solution:
    def numberOfMatches(self, n: int) -> int:
        def helper(n, r):
            if n<=1:
                return r
            if n%2==0:
                return helper(n//2, r+n//2)
            else:
                return helper(1+n//2, r+n//2)
        return helper(n, 0)

class Solution:
    def numberOfMatches(self, n: int) -> int:
        r = 0
        while n!=1:
            if n%2==0:
                r += n//2
                n = n//2
            else:
                r += (n-1)//2
                n = (n-1)//2 + 1
        return r

class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1

class Solution:
    def numberOfMatches(self, n: int) -> int:
        return~-n

test('''
1688. Count of Matches in Tournament
Easy

1046

165

Add to List

Share
You are given an integer n, the number of teams in a tournament that has strange rules:

If the current number of teams is even, each team gets paired with another team. A total of n / 2 matches are played, and n / 2 teams advance to the next round.
If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.
Return the number of matches played in the tournament until a winner is decided.

 

Example 1:

Input: n = 7
Output: 6
Explanation: Details of the tournament: 
- 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
- 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 3 + 2 + 1 = 6.
Example 2:

Input: n = 14
Output: 13
Explanation: Details of the tournament:
- 1st Round: Teams = 14, Matches = 7, and 7 teams advance.
- 2nd Round: Teams = 7, Matches = 3, and 4 teams advance.
- 3rd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 4th Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 7 + 3 + 2 + 1 = 13.
 

Constraints:

1 <= n <= 200
Accepted
115,373
Submissions
138,874
''')

