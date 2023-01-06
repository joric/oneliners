from lc import *

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i, a in enumerate(costs):
            coins -= a
            if coins < 0:
                return i
        return len(costs)

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return next((i for i,a in enumerate(sorted(costs)) if (coins:=coins-a) and coins<0),len(costs))

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return next((i for i, x in enumerate(accumulate(sorted(costs))) if x>coins), len(costs))

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return len(list(takewhile(partial(ge, coins), accumulate(sorted(costs)))))

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return sum(1 for c in sorted(costs) if (coins:=coins-c)>=0)

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return bisect_right(list(accumulate(sorted(costs))), coins)

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        r, q = 0, Counter(costs)
        for c in range(1, max(costs) + 1):
            if not q[c]:
                continue
            if coins < c:
                break
            t = min(q[c],coins//c)
            coins -= c*t
            r += t
        return r

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return (r:=0,q:=Counter(costs),[q[c] and coins>=c and (t:=min(q[c],coins//c), coins:=coins-c*t, r:=r+t) for c in range(1,max(costs)+1)]) and r

test('''

1833. Maximum Ice Cream Bars
Medium

466

194

Add to List

Share
It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

Return the maximum number of ice cream bars the boy can buy with coins coins.

Note: The boy can buy the ice cream bars in any order.

 

Example 1:

Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
Example 2:

Input: costs = [10,6,8,7,7,8], coins = 5
Output: 0
Explanation: The boy cannot afford any of the ice cream bars.
Example 3:

Input: costs = [1,6,3,1,2,5], coins = 20
Output: 6
Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.
 

Constraints:

costs.length == n
1 <= n <= 10^5
1 <= costs[i] <= 10^5
1 <= coins <= 10^8

''')

