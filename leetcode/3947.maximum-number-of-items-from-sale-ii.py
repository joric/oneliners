from lc import *

# https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/solutions/8303681/w504-q3-python-solution-by-__abhinavarya-lok5/?envType=daily-question&envId=2026-11-28

class Solution:
    def maximumSaleItems(self, a: List[List[int]], b: int) -> int:
        n = len(a)
        vals = [x[0] for x in a]
        freq = Counter(vals)
        mx = max(vals)
        factor = {}
        for v in freq:
            c = 0 
            m = v 
            while m <= mx: 
                if m in freq: c += freq[m]
                m += v 
            c -= 1 
            factor[v] = c 
        pre = []
        mn = inf
        for i in range(n):
            v, cost = a[i]
            c = factor[v]
            pre.append([v, cost, c, cost/(2 if c > 0 else 1)])
            mn = min(mn, cost)
        pre.sort(key=lambda x:(x[3],-x[2]))
        res = b//mn 
        cnt = 0 
        i = 1 
        for x, y, z, w in pre: 
            c = min(z, (b // y))
            cnt += c*2
            b -= c*y 
            res = max(res, cnt + (b//mn))
        return res

class Solution: # TLE
    def maximumSaleItems(self, a: List[List[int]], b: int) -> int:
        m=min(p for _,p in a);r=b//m;k=0;[r:=max(r,(k:=k+2*(c:=min(-q,b//p)))+(b:=b-c*p)//m)for w,q,p in sorted((p/(1+(q<0)),q,p)for v,p in a for q in[1-sum(y%v<1for y,_ in a)])];return r

class Solution:
    def maximumSaleItems(self, a: List[List[int]], b: int) -> int:
        c=Counter(v for v,_ in a);t=max(c);e={v:1-sum(c[m]for m in range(v,-~t,v))for v in c};m=min(p for _,p in a);r=b//m;k=0;[r:=max(r,(k:=k+2*(c:=min(-q,b//p)))+(b:=b-c*p)//m)for w,q,p in sorted((p/(1+(e[v]<0)),e[v],p)for v,p in a)];return r

class Solution:
    def maximumSaleItems(self, a: List[List[int]], b: int) -> int:
        f,g=zip(*a);c=Counter(f);t=max(f);e={v:1-sum(c[m]for m in range(v,-~t,v))for v in c};m=min(g);k=0;return max(b//m,*[(b:=b-(c:=min(-q,b//p))*p)//m+(k:=k+2*c)for w,q,p in sorted((p/2**(e[v]<0),e[v],p)for v,p in a)])

class Solution:
    def maximumSaleItems(self, a: List[List[int]], b: int) -> int:
        f,g=zip(*a);c=Counter(f);e={v:1-sum(c[m]for m in range(v,-~len(a),v))for v in c};m=min(g);k=0;return max(b//m,*[(b:=b-(c:=min(-q,b//p))*p)//m+(k:=k+2*c)for w,q,p in sorted((p/2**(e[v]<0),e[v],p)for v,p in a)])

test('''
3947. Maximum Number of Items From Sale II
Medium
Topics
premium lock icon
Companies
Hint
You are given a 2D integer array items, where items[i] = [factori, pricei] represents the ith item. You are also given an integer budget.

There are unlimited copies of each item available for purchase. You may buy any number of copies of any items such that the total cost of the purchased copies is at most budget.

After buying items, you may receive free copies according to the following rules:

Each purchased copy of item i can give you at most one free copy of another item j.
The free item must satisfy i != j and factori divides factorj.
For each ordered pair (i, j), you can receive a free copy of item j from purchases of item i at most once, regardless of how many copies of item i you buy.
The same item j can be received multiple times for free if it is received from purchases of different item types.
Return the maximum total number of item copies you can obtain, including both purchased copies and free copies, while spending at most budget on purchased items.

 

Example 1:

Input: items = [[1,6],[2,4],[3,5]], budget = 19

Output: 5

Explanation:

You can buy 2 copies of item 0 and 1 copy of item 1 for a total cost of 2 * 6 + 4 = 16, which is not greater than budget = 19.
One purchased copy of item 0 gives 1 free copy of item 1, because factor0 = 1 divides factor1 = 2.
The other purchased copy of item 0 gives 1 free copy of item 2, because factor0 = 1 divides factor2 = 3.
You leave with 3 purchased copies and 2 free copies, for a total of 5 item copies.
Example 2:

Input: items = [[2,8],[1,10],[6,6],[4,12],[5,20],[5,17]], budget = 35

Output: 7

Explanation:

You can buy 2 copies of item 0, 1 copy of item 1, and 1 copy of item 2 for a total cost of 2 * 8 + 10 + 6 = 32, which is not greater than budget = 35.
One purchased copy of item 0 gives 1 free copy of item 2, because factor0 = 2 divides factor2 = 6.
The other purchased copy of item 0 gives 1 free copy of item 3, because factor0 = 2 divides factor3 = 4.
The purchased copy of item 1 gives 1 free copy of item 2, because factor1 = 1 divides factor2 = 6.
Buying item 2 gives no free copy, because factor2 = 6 does not divide the factor of any other item.
You leave with 4 purchased copies and 3 free copies, for a total of 7 item copies.
 

Constraints:

1 <= items.length <= 105
items[i] = [factori, pricei]
1 <= factori <= items.length
1 <= pricei <= 109
1 <= budget <= 109
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
7,547/24.1K
Acceptance Rate
31.3%
Topics
Staff
Array
Greedy
Sorting
Heap (Priority Queue)
Weekly Contest 504
icon
Companies
Hint 1
For each item i, compute gain[i] = number of other items j such that factor[i] divides factor[j]. This can be done by counting factors and iterating over multiples.
Hint 2
If you buy c copies of item i, it contributes c + min(c, gain[i]) total copies, because only the first gain[i] purchased copies can be matched to distinct free items.
Hint 3
View purchases as marginal units: for item i, the first gain[i] copies have value 2 each, and all later copies have value 1 each.
Hint 4
Since extra value-1 copies should always be bought from the cheapest item, the main task is to choose the cheapest useful value-2 marginal units. Sort item types by price and process their gain[i] boosted copies in batches rather than expanding them one by one.
''')
