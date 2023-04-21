from lc import *

# https://leetcode.com/problems/profitable-schemes/discuss/154617/C%2B%2BJavaPython-DP

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[0] * (n + 1) for i in range(minProfit + 1)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            for i in range(minProfit, -1, -1):
                for j in range(n - g, -1, -1):
                    dp[min(i + p, minProfit)][j + g] += dp[i][j]
        return sum(dp[minProfit]) % (10**9+7)

# https://leetcode.com/problems/profitable-schemes/discuss/563888/4-line-python-DP-solution

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @cache
        def f(i, g, p):
            return ((f(i - 1, g, p) + (f(i - 1, g - group[i], max(0, p - profit[i])) if g >= group[i] else 0)) % 1000000007) if i >= 0 and g > 0 else int(p <= 0)
        return f(len(group) - 1, n, minProfit) 

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        return (f:=cache(lambda i,g,p:((f(i-1,g,p)+(f(i-1,g-group[i],max(0,p-profit[i])) if g>=group[i] else 0))%(10**9+7)) if i>=0 and g>0 else int(p<=0)))(len(group)-1,n,minProfit)

class Solution:
    def profitableSchemes(self, n: int, m: int, r: List[int], t: List[int]) -> int:
        return (f:=cache(lambda i,g,p:((f(i-1,g,p)+(f(i-1,g-r[i],max(0,p-t[i])) if g>=r[i] else 0))%(10**9+7)) if i>=0 and g>0 else int(p<=0)))(len(r)-1,n,m)

class Solution:
    def profitableSchemes(self, n: int, m: int, r: List[int], t: List[int]) -> int:
        return (f:=cache(lambda i,g,p:i+1 and g and (f(i-1,g,p)+(g>=r[i] and f(i-1,g-r[i],max(0,p-t[i])))) or p<=0))(len(r)-1,n,m)%(10**9+7)

test('''
879. Profitable Schemes
Hard

597

48

Add to List

Share
There is a group of n members, and a list of various crimes they could commit. The ith crime generates a profit[i] and requires group[i] members to participate in it. If a member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, and the total number of members participating in that subset of crimes is at most n.

Return the number of schemes that can be chosen. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.
Example 2:

Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation: To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).
 

Example 3:
Input: n = 1, minProfit = 1, group = [1,1,1,1,2,2,1,2,1,1], profit = [0,1,0,0,1,1,1,0,2,2]
Output: 4

Example 4:
Input: n = 1, minProfit = 1, group = [2,2,2,2,2], profit = [1,2,1,1,0]
Output: 0

Constraints:

1 <= n <= 100
0 <= minProfit <= 100
1 <= group.length <= 100
1 <= group[i] <= 100
profit.length == group.length
0 <= profit[i] <= 100
Accepted
18,113
Submissions
44,474
''')
