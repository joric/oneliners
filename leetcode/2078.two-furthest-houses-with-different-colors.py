from lc import *

# https://leetcode.com/problems/two-furthest-houses-with-different-colors/solutions/5007348/python-two-line-solution-beats-95-by-nei-ka7s/?envType=daily-question&envId=2026-04-20

class Solution:
    def maxDistance(self, c: List[int]) -> int:
        return max(j-i for i in range(len(c))for j in range(i+1,len(c))if c[i]!=c[j])

class Solution:
    def maxDistance(self, c: List[int]) -> int:
        return next(~i+len(c)for i,x in enumerate(c)if c[0]!=c[~i]or c[-1]!=x)

class Solution:
    def maxDistance(self, c: List[int]) -> int:
        return max(j-i for i,j in product(*[range(len(c))]*2)if c[i]!=c[j])

class Solution:
    def maxDistance(self, c: List[int]) -> int:
        return max(i for i,x in enumerate(c)if x!=c[0]or c[-1]!=c[~i])

class Solution:
    def maxDistance(self, c: List[int]) -> int:
        return max(i*(x!=c[0]or c[-1]!=c[~i])for i,x in enumerate(c))

test('''
2078. Two Furthest Houses With Different Colors
Easy
Topics
premium lock icon
Companies
Hint
There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

Return the maximum distance between two houses with different colors.

The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.

 

Example 1:


Input: colors = [1,1,1,6,1,1,1]
Output: 3
Explanation: In the above image, color 1 is blue, and color 6 is red.
The furthest two houses with different colors are house 0 and house 3.
House 0 has color 1, and house 3 has color 6. The distance between them is abs(0 - 3) = 3.
Note that houses 3 and 6 can also produce the optimal answer.
Example 2:


Input: colors = [1,8,3,8,3]
Output: 4
Explanation: In the above image, color 1 is blue, color 8 is yellow, and color 3 is green.
The furthest two houses with different colors are house 0 and house 4.
House 0 has color 1, and house 4 has color 3. The distance between them is abs(0 - 4) = 4.
Example 3:

Input: colors = [0,1]
Output: 1
Explanation: The furthest two houses with different colors are house 0 and house 1.
House 0 has color 0, and house 1 has color 1. The distance between them is abs(0 - 1) = 1.

Other examples:

Input: colors = [6,6,6,6,6,6,6,6,6,19,19,6,6]
Output: 10

Constraints:

n == colors.length
2 <= n <= 100
0 <= colors[i] <= 100
Test data are generated such that at least two houses have different colors.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
95,096/145.2K
Acceptance Rate
65.5%
Topics
Mid Level
Array
Greedy
Weekly Contest 268
icon
Companies
Hint 1
The constraints are small. Can you try the combination of every two houses?
Hint 2
Greedily, the maximum distance will come from either the pair of the leftmost house and possibly some house on the right with a different color, or the pair of the rightmost house and possibly some house on the left with a different color.
Similar Questions
Replace Elements with Greatest Element on Right Side
Easy
Maximum Distance Between a Pair of Values
Medium
Maximum Difference Between Increasing Elements
Easy
''')
