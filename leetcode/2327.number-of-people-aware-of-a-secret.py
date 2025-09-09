from lc import *

# https://leetcode.com/problems/number-of-people-aware-of-a-secret/solutions/2230188/python-4-lines/?envType=daily-question&envId=2025-09-09

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [[1, 0]] + [[0, 0] for _ in range(n - 1)]
        for i in range(1, n):
            dp[i] = [sum([i[0] for i in dp[max(0, i - forget + 1) : max(0, i - delay + 1)]]), dp[i - forget][0]]
        return sum([i[0] - i[1] for i in dp]) % (10 ** 9 + 7)

class Solution:
    def peopleAwareOfSecret(self, n: int, d: int, f: int) -> int:
        p=[[1,0]]+[[0,0] for _ in range(n-1)]
        for i in range(1,n):
            p[i]=[sum([i[0]for i in p[max(0,i-f+1):max(0,i-d+1)]]),p[i-f][0]]
        return sum([i[0]-i[1]for i in p])%(10 ** 9 + 7)

class Solution:
    def peopleAwareOfSecret(self, n: int, d: int, f: int) -> int:
        p=[[1,0]]+[[0,0]for _ in range(n-1)];[setitem(p,i,[sum([i[0]for i in p[max(0,i-f+1):max(0,i-d+1)]]),p[i-f][0]])for i in range(1,n)];return sum([i[0]-i[1]for i in p])%(10**9+7)

# https://leetcode.com/problems/number-of-people-aware-of-a-secret/solutions/2229982/java-c-python-sliding-window-o-n-time-o-forget-space/?envType=daily-question&envId=2025-09-09

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [1] + [0] * (n - 1)
        mod = 10 ** 9 + 7
        share = 0
        for i in range(1, n):
            dp[i] = share = (share + dp[i - delay] - dp[i - forget]) % mod
        return sum(dp[-forget:]) % mod

class Solution:
    def peopleAwareOfSecret(self, n: int, d: int, f: int) -> int:
        p,s=[1]+[0]*~-n,0;[setitem(p,i,s:=(s+p[i-d]-p[i-f]))for i in range(1,n)];return sum(p[-f:])%(10**9+7)

test('''
2327. Number of People Aware of a Secret
Solved
Medium
Topics
premium lock icon
Companies
Hint
On day 1, one person discovers a secret.

You are given an integer delay, which means that each person will share the secret with a new person every day, starting from delay days after discovering the secret. You are also given an integer forget, which means that each person will forget the secret forget days after discovering it. A person cannot share the secret on the same day they forgot it, or on any day afterwards.

Given an integer n, return the number of people who know the secret at the end of day n. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 6, delay = 2, forget = 4
Output: 5
Explanation:
Day 1: Suppose the first person is named A. (1 person)
Day 2: A is the only person who knows the secret. (1 person)
Day 3: A shares the secret with a new person, B. (2 people)
Day 4: A shares the secret with a new person, C. (3 people)
Day 5: A forgets the secret, and B shares the secret with a new person, D. (3 people)
Day 6: B shares the secret with E, and C shares the secret with F. (5 people)
Example 2:

Input: n = 4, delay = 1, forget = 3
Output: 6
Explanation:
Day 1: The first person is named A. (1 person)
Day 2: A shares the secret with B. (2 people)
Day 3: A and B share the secret with 2 new people, C and D. (4 people)
Day 4: A forgets the secret. B, C, and D share the secret with 3 new people. (6 people)
 

Constraints:

2 <= n <= 1000
1 <= delay < forget <= n
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
31,996/66.8K
Acceptance Rate
47.9%
Topics
Dynamic Programming
Queue
Simulation
Weekly Contest 300
icon
Companies
Hint 1
Let dp[i][j] be the number of people who have known the secret for exactly j + 1 days, at day i.
Hint 2
If j > 0, dp[i][j] = dp[i – 1][j – 1].
Hint 3
dp[i][0] = sum(dp[i – 1][j]) for j in [delay – 1, forget – 2].
''')
