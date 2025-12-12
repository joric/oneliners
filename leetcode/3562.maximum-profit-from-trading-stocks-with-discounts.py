from lc import *

# https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/solutions/6778680/python-dp-on-tree-by-awice-e99b/

fmax = lambda x, y: x if x > y else y

def merge(A, B):
    C = [-inf] * len(A)
    for i, a in enumerate(A):
        for j in range(len(A) - i):
            C[i + j] = fmax(C[i + j], a + B[j])
    return C

class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:

        adj = [[] for _ in range(n)]
        for u, v in hierarchy:
            u -= 1
            v -= 1
            adj[u].append(v)

        def dfs(u, p):
            # res0[b] : max profit for budget b with no discount
            # res1[b] : max profit for budget b with this node discounted
            dp0 = [0] * (budget + 1)
            dp1 = [0] * (budget + 1)
            for v in adj[u]:
                if v != p:
                    res0, res1 = dfs(v, u)
                    dp0, dp1 = merge(dp0, res0), merge(dp1, res1)

            ans0 = dp0[:]
            ans1 = dp0[:]

            cost = present[u]
            for b in range(cost, budget + 1):
                ans0[b] = fmax(ans0[b], dp1[b - cost] + future[u] - cost)

            cost >>= 1
            for b in range(cost, budget + 1):
                ans1[b] = fmax(ans1[b], dp1[b - cost] + future[u] - cost)

            return ans0, ans1

        return max(dfs(0, -1)[0])

# TODO

class Solution:
    def maxProfit(self, n: int, p: List[int], f: List[int], h: List[List[int]], b: int) -> int:
        t = [[] for _ in range(n)]
        [t[u-1].append(v-1)for u,v in h]
        h=lambda x,y:(z:=[-inf]*len(x),[setitem(z,i+j,max(z[i+j],a+y[j]))for i,a in enumerate(x)for j in range(len(x)-i)])[0]

        def z(u, q):
            x = [0]*(b+1)
            y = [0]*(b+1)

            for v in t[u]:
                if v!=q:
                    r, s = z(v, u)
                    x, y = h(x, r), h(y, s)


            g=lambda c:(r:=x[:],[setitem(r,k,max(r[k],y[k-c]+f[u]-c))for k in range(c,b+1)])[0]
            return g(p[u]),g(p[u]>>1)

        return max(z(0,-1)[0])



test('''
3562. Maximum Profit from Trading Stocks with Discounts
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer n, representing the number of employees in a company. Each employee is assigned a unique ID from 1 to n, and employee 1 is the CEO. You are given two 1-based integer arrays, present and future, each of length n, where:

present[i] represents the current price at which the ith employee can buy a stock today.
future[i] represents the expected price at which the ith employee can sell the stock tomorrow.
The company's hierarchy is represented by a 2D integer array hierarchy, where hierarchy[i] = [ui, vi] means that employee ui is the direct boss of employee vi.

Additionally, you have an integer budget representing the total funds available for investment.

However, the company has a discount policy: if an employee's direct boss purchases their own stock, then the employee can buy their stock at half the original price (floor(present[v] / 2)).

Return the maximum profit that can be achieved without exceeding the given budget.

Note:

You may buy each stock at most once.
You cannot use any profit earned from future stock prices to fund additional investments and must buy only from budget.
 

Example 1:

Input: n = 2, present = [1,2], future = [4,3], hierarchy = [[1,2]], budget = 3

Output: 5

Explanation:



Employee 1 buys the stock at price 1 and earns a profit of 4 - 1 = 3.
Since Employee 1 is the direct boss of Employee 2, Employee 2 gets a discounted price of floor(2 / 2) = 1.
Employee 2 buys the stock at price 1 and earns a profit of 3 - 1 = 2.
The total buying cost is 1 + 1 = 2 <= budget. Thus, the maximum total profit achieved is 3 + 2 = 5.
Example 2:

Input: n = 2, present = [3,4], future = [5,8], hierarchy = [[1,2]], budget = 4

Output: 4

Explanation:



Employee 2 buys the stock at price 4 and earns a profit of 8 - 4 = 4.
Since both employees cannot buy together, the maximum profit is 4.
Example 3:

Input: n = 3, present = [4,6,8], future = [7,9,11], hierarchy = [[1,2],[1,3]], budget = 10

Output: 10

Explanation:



Employee 1 buys the stock at price 4 and earns a profit of 7 - 4 = 3.
Employee 3 would get a discounted price of floor(8 / 2) = 4 and earns a profit of 11 - 4 = 7.
Employee 1 and Employee 3 buy their stocks at a total cost of 4 + 4 = 8 <= budget. Thus, the maximum total profit achieved is 3 + 7 = 10.
Example 4:

Input: n = 3, present = [5,2,3], future = [8,5,6], hierarchy = [[1,2],[2,3]], budget = 7

Output: 12

Explanation:



Employee 1 buys the stock at price 5 and earns a profit of 8 - 5 = 3.
Employee 2 would get a discounted price of floor(2 / 2) = 1 and earns a profit of 5 - 1 = 4.
Employee 3 would get a discounted price of floor(3 / 2) = 1 and earns a profit of 6 - 1 = 5.
The total cost becomes 5 + 1 + 1 = 7 <= budget. Thus, the maximum total profit achieved is 3 + 4 + 5 = 12.
 

Constraints:

1 <= n <= 160
present.length, future.length == n
1 <= present[i], future[i] <= 50
hierarchy.length == n - 1
hierarchy[i] == [ui, vi]
1 <= ui, vi <= n
ui != vi
1 <= budget <= 160
There are no duplicate edges.
Employee 1 is the direct or indirect boss of every employee.
The input graph hierarchy is guaranteed to have no cycles.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
4,087/18.2K
Acceptance Rate
22.5%
Topics
Array
Dynamic Programming
Tree
Depth-First Search
Weekly Contest 451
icon
Companies
Hint 1
- Compute max_profit[u] and max_profit1[u] for each node u
Hint 2
- max_profit[u] = maximum profit in the subtree of u assuming the parent of u has not bought the stock
Hint 3
- max_profit1[u] = maximum profit in the subtree of u assuming the parent of u has bought the stock
Hint 4
For each node u, consider two cases:
Hint 5
Buy the stock for u (at present[u] price if parent did not buy, or at floor(present[u]/2) if parent bought), then add the best max_profit1 values of its children
Hint 6
Skip buying for u, then add the best max_profit values of its children
''')
