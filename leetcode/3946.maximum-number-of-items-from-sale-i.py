from lc import *

# https://leetcode.com/problems/maximum-number-of-items-from-sale-i/solutions/8303642/w504-q2-python-solution-by-__abhinavarya-t7uk/?envType=daily-question&envId=2026-11-27

class Solution:
    def maximumSaleItems(self, a: List[List[int]], b: int) -> int:
        n = len(a)
        c = []
        for i in range(n):
            x = 1
            for j in range(n):
                if i == j: continue 
                if a[j][0]%a[i][0] == 0: 
                    x += 1 
            c.append(a[i] + [x])
        d = [0] * (b+1)
        for i in range(n):
            p = c[i][1]
            x = c[i][2]
            for j in range(p, b+1):
                d[j] = max(d[j], d[j-p]+1)
            for j in range(j, p-1, -1):
                d[j] = max(d[j], d[j-p]+x)
        return max(d)

class Solution:
    def maximumSaleItems(self, a: List[List[int]], b: int) -> int:
        d=[0]*-~b;[setitem(d,j,max(d[j],d[j-p]+x))for v,p in a for x in(1,sum(y%v<1for y,_ in a))for j in range(p,b+1)[::x<2or-1]];return d[b]

test('''
3946. Maximum Number of Items From Sale I
Medium
Topics
premium lock icon
Companies
Hint
You are given a 2D integer array items, where items[i] = [factori, pricei] represents the ith item. You are also given an integer budget.

There are unlimited copies of each item available for purchase.You may buy any number of copies of any items such that the total cost of the purchased copies is at most budget.

After buying items, you may receive free copies according to the following rules:

For each item i that you bought at least one copy of, you receive one free copy of every item j such that j != i and factori divides factorj.
Buying multiple copies of the same item i does not give additional free copies through item i.
The same item j can be received multiple times for free if it is received from purchases of different item types.
Return the maximum total number of item copies you can obtain, including both purchased copies and free copies, while spending at most budget on purchased items.

 

Example 1:

Input: items = [[6,2],[2,6],[3,4]], budget = 9

Output: 4

Explanation:

You can buy 2 copies of item 0 and 1 copy of item 2 for a total cost of 2 * 2 + 4 = 8, which is not greater than budget = 9.
Buying item 2 gives 1 free copy of item 0, because factor2 = 3 divides factor0 = 6.
You leave with 3 purchased copies and 1 free copy, for a total of 4 item copies.
Example 2:

Input: items = [[2,4],[3,2],[4,1],[6,4],[12,4]], budget = 8

Output: 10

Explanation:

You can buy 1 copy of item 0, 1 copy of item 1, and 2 copies of item 2 for a total cost of 4 + 2 + 2 * 1 = 8.
Buying item 0 gives 1 free copy of items 2, 3, and 4.
Buying item 1 gives 1 free copy of items 3 and 4.
Buying item 2 gives 1 free copy of item 4.
Thus, you receive 6 free copies. You leave with 4 purchased copies and 6 free copies, for a total of 10 item copies.
 

Constraints:

1 <= items.length <= 1000
items[i] = [factori, pricei]
1 <= factori, pricei <= 1500
1 <= budget <= 1500
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
22,235/59.9K
Acceptance Rate
37.1%
Topics
Staff
Array
Dynamic Programming
Greedy
Weekly Contest 504
icon
Companies
Hint 1
Precompute for every possible factor f, how many items have a factor divisible by f.
Hint 2
Buying the first copy of item i is special: it gives the purchased copy plus one free copy of every other item whose factor is divisible by factor_i.
Hint 3
Buying more copies of the same item does not create more free copies, so after the first copy, each extra purchase only adds one item copy.
Hint 4
This suggests a knapsack-style DP over item types and remaining budget, where each item can either be skipped, bought for the first time, or bought additional times after it has already been activated.
''')
