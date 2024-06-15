from lc import *

# https://leetcode.com/problems/ipo/discuss/98223/Python-solution

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        c,f = [],sorted(zip(capital, profits))[::-1]
        for _ in range(k):
            while f and f[-1][0] <= w:
                heappush(c,-f.pop()[1])
            if c:
                w -= heappop(c)
        return w

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        return (c:=[],f:=sorted(zip(capital,profits))[::-1],[next(c and (w:=w-heappop(c)) for _ in count() if not(f and f[-1][0]<=w and not heappush(c,-f.pop()[1]))) for _ in range(k)],w)[-1]

# updated 2024-06-15

class Solution:
    def findMaximizedCapital(self, k: int, w: int, p: List[int], c: List[int]) -> int:
        h,q = [],sorted(zip(c,p))[::-1]
        for _ in range(k):
            while q and q[-1][0] <= w:
                heappush(h,-q.pop()[1])
            if h:
                w -= heappop(h)
        return w

class Solution:
    def findMaximizedCapital(self, k: int, w: int, p: List[int], c: List[int]) -> int:
        h,q=[],sorted(zip(c,p))[::-1];[(all(q and q[-1][0]<=w and[heappush(h,-q.pop()[1])]for _ in p),h and(w:=w-heappop(h)))for _ in range(k)];return w

test('''
502. IPO
Hard

1384

110

Add to List

Share
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.

 

Example 1:

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Example 2:

Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6
 

Constraints:

1 <= k <= 10^5
0 <= w <= 10^9
n == profits.length
n == capital.length
1 <= n <= 10^5
0 <= profits[i] <= 10^4
0 <= capital[i] <= 10^9
''')
