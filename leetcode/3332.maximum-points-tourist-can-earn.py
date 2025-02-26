from lc import *

# https://leetcode.com/problems/maximum-points-tourist-can-earn/solutions/5997049/recursion-explained-not-opti-but-beginner-friendly/

class Solution:
    def maxScore(self, n: int, k: int, s: List[List[int]], t: List[List[int]]) -> int:
        f=cache(lambda i,k,c:k>0 and max((t[c][j],s[i][c])[j==c]+f(i+1,k-1,j)for j in range(n))or 0);return max(f(0,k,i)for i in range(n))

test('''
3332. Maximum Points Tourist Can Earn
Solved
Medium
Topics
Companies
Hint
You are given two integers, n and k, along with two 2D integer arrays, stayScore and travelScore.

A tourist is visiting a country with n cities, where each city is directly connected to every other city. The tourist's journey consists of exactly k 0-indexed days, and they can choose any city as their starting point.

Each day, the tourist has two choices:

Stay in the current city: If the tourist stays in their current city curr during day i, they will earn stayScore[i][curr] points.
Move to another city: If the tourist moves from their current city curr to city dest, they will earn travelScore[curr][dest] points.
Return the maximum possible points the tourist can earn.

 

Example 1:

Input: n = 2, k = 1, stayScore = [[2,3]], travelScore = [[0,2],[1,0]]

Output: 3

Explanation:

The tourist earns the maximum number of points by starting in city 1 and staying in that city.

Example 2:

Input: n = 3, k = 2, stayScore = [[3,4,2],[2,1,2]], travelScore = [[0,2,1],[2,0,4],[3,2,0]]

Output: 8

Explanation:

The tourist earns the maximum number of points by starting in city 1, staying in that city on day 0, and traveling to city 2 on day 1.

 

Constraints:

1 <= n <= 200
1 <= k <= 200
n == travelScore.length == travelScore[i].length == stayScore[i].length
k == stayScore.length
1 <= stayScore[i][j] <= 100
0 <= travelScore[i][j] <= 100
travelScore[i][i] == 0
Seen this question in a real interview before?
1/5
Yes
No
Accepted
12K
Submissions
24.4K
Acceptance Rate
49.4%
Topics
Array
Dynamic Programming
Matrix
Companies
Hint 1
Use DP.
Hint 2
''')
