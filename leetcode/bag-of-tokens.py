from lc import *

# https://leetcode.com/problems/bag-of-tokens/discuss/2566293/Python-short-(6-lines)-faster-than-96-(54-ms)

class Solution:
    def bagOfTokensScore(self, t: List[int], p: int) -> int:
        r=c=0
        d = deque(sorted(t))
        while d and (d[0]<=p or c):
            if d[0]<=p:
                p -= d.popleft()
                c += 1
            else:
                p += d.pop()
                c -= 1
            r = max(r,c)
        return r

class Solution:
    def bagOfTokensScore(self, t: List[int], p: int) -> int:
        c=r=0
        d=deque(sorted(t))
        while d and (d[0]<=p or c):
            (d[0]<=p and (p:=p-d.popleft(),c:=c+1)or(p:=p+d.pop(),c:=c-1),r:=max(r,c))
        return r

class Solution:
    def bagOfTokensScore(self, t: List[int], p: int) -> int:
        c=r=0;d=deque(sorted(t));return next(r for _ in count()if not(d and(p>=d[0]or c)and(p>=d[0]and(p:=p-d.popleft(),c:=c+1)or(p:=p+d.pop(),c:=c-1),r:=max(r,c))))

test('''
948. Bag of Tokens
Medium

2613

466

Add to List

Share
You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens, where each tokens[i] donates the value of tokeni.

Your goal is to maximize the total score by strategically playing these tokens. In one move, you can play an unplayed token in one of the two ways (but not both for the same token):

Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.
Return the maximum possible score you can achieve after playing any number of tokens.

 

Example 1:

Input: tokens = [100], power = 50

Output: 0

Explanation: Since your score is 0 initially, you cannot play the token face-down. You also cannot play it face-up since your power (50) is less than tokens[0] (100).

Example 2:

Input: tokens = [200,100], power = 150

Output: 1

Explanation: Play token1 (100) face-up, reducing your power to 50 and increasing your score to 1.

There is no need to play token0, since you cannot play it face-up to add to your score. The maximum score achievable is 1.

Example 3:

Input: tokens = [100,200,300,400], power = 200

Output: 2

Explanation: Play the tokens in this order to get a score of 2:

Play token0 (100) face-up, reducing power to 100 and increasing score to 1.
Play token3 (400) face-down, increasing power to 500 and reducing score to 0.
Play token1 (200) face-up, reducing power to 300 and increasing score to 1.
Play token2 (300) face-up, reducing power to 0 and increasing score to 2.
The maximum score achievable is 2.

 

Constraints:

0 <= tokens.length <= 1000
0 <= tokens[i], power < 104
Accepted
137,392
Submissions
250,146
''')
