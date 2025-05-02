from lc import *

# https://leetcode.com/problems/push-dominoes/solutions/5967314/one-line-solution/?envType=daily-question&envId=2025-05-02

class Solution:
    def pushDominoes(self, s: str) -> str:
        return re.sub(r'(?<=R)(\.+)(?=L)',lambda m:(q:=len(m[1]))//2*'R'+q%2*'.'+q//2*'L',re.sub(r'(R|L)(\.+)(?=\1)',lambda m:m[1]*(len(m[2])+1),f'L{s}R'))[1:-1]

class Solution:
    def pushDominoes(self, s: str) -> str:
        return re.sub(r'R?\.+L?',lambda m:{'RL':(l:=len(s:=m[0]))//2*'R'+l%2*'.'+l//2*'L','R.':'R'*l,'.L':'L'*l}.get(s[0]+s[-1],s),s)

class Solution:
    def pushDominoes(self, s: str) -> str:
        return all(s!=(s:=s.replace('R.L','*').replace('R.','RR').replace('.L','LL'))for _ in s)or s.replace('*','R.L')

test('''
838. Push Dominoes
Solved
Medium
Topics
Companies
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

 

Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:


Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
 

Constraints:

n == dominoes.length
1 <= n <= 105
dominoes[i] is either 'L', 'R', or '.'.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
156.6K
Submissions
262.8K
Acceptance Rate
59.6%
Topics
Two Pointers
String
Dynamic Programming
''')
