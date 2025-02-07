from lc import *

# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/solutions/5207199/easy-and-fast/?envType=daily-question&envId=2025-02-07
# can't do +c to clear keys because TLE

class Solution:
    def queryResults(self, limit: int, q: List[List[int]]) -> List[int]:
        r,b,c = [],Counter(),Counter()
        for x, y in q:
            p = b[x]
            c[p] -= 1
            if c[p]<1:
                c.pop(p)
            b[x] = y
            c[y] += 1
            r.append(len(c))
        return r

class Solution:
    def queryResults(self, limit: int, q: List[List[int]]) -> List[int]:
        r,b,c = [],Counter(),Counter()
        for x, y in q:
            c.update({b[x]:-1})
            c[b[x]]<1 and c.pop(b[x])
            setitem(b,x,y)
            c.update([y])
            r.append(len(c))
        return r

class Solution:
    def queryResults(self, limit: int, q: List[List[int]]) -> List[int]:
        t=Counter;b,c=t(),t();return[(p:=b[x],c.update({p:-1}),0<c[p]or c.pop(p),setitem(b,x,y),c.update([y]),len(c))[5]for x,y in q]

class Solution:
    def queryResults(self, limit: int, q: List[List[int]]) -> List[int]:
        t=Counter;b,c=t(),t();return[(p:=b[x],c.update({p:-1,y:p!=y}),0<c[p]or c.pop(p),setitem(b,x,y),len(c))[4]for x,y in q]

test('''
3160. Find the Number of Distinct Colors Among the Balls
Medium
Topics
Companies
Hint
You are given an integer limit and a 2D array queries of size n x 2.

There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of distinct colors among the balls.

Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.

Note that when answering a query, lack of a color will not be considered as a color.

 

Example 1:

Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]

Output: [1,2,2,3]

Explanation:



After query 0, ball 1 has color 4.
After query 1, ball 1 has color 4, and ball 2 has color 5.
After query 2, ball 1 has color 3, and ball 2 has color 5.
After query 3, ball 1 has color 3, ball 2 has color 5, and ball 3 has color 4.
Example 2:

Input: limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]

Output: [1,2,2,3,4]

Explanation:



After query 0, ball 0 has color 1.
After query 1, ball 0 has color 1, and ball 1 has color 2.
After query 2, ball 0 has color 1, and balls 1 and 2 have color 2.
After query 3, ball 0 has color 1, balls 1 and 2 have color 2, and ball 3 has color 4.
After query 4, ball 0 has color 1, balls 1 and 2 have color 2, ball 3 has color 4, and ball 4 has color 5.
 

Other examples:

Input: limit = 1, queries = [[0,2],[1,10],[0,10],[0,3],[1,5]]
Output: [1,2,1,2,2]


Input: limit = 1, queries = [[0,1],[0,4],[0,4],[0,1],[1,2]]
Output: [1,1,1,1,2]

Constraints:

1 <= limit <= 109
1 <= n == queries.length <= 105
queries[i].length == 2
0 <= queries[i][0] <= limit
1 <= queries[i][1] <= 109
Seen this question in a real interview before?
1/5
Yes
No
Accepted
26.7K
Submissions
64.9K
Acceptance Rate
41.2%
Topics
Array
Hash Table
Simulation
Companies
Hint 1
Use two HashMaps to maintain the color of each ball and the set of balls with each color.
Similar Questions
Maximum Number of Balls in a Box
Easy
''')
