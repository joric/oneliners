from lc import * 

# https://leetcode.com/problems/maximum-distance-in-arrays/discuss/5642974/python-one-line-solution

class Solution:
    def maxDistance(self, a: List[List[int]]) -> int:
        return reduce(lambda a,b:(min(b[0],a[0]),max(b[-1], a[1]),max(a[2],a[1]-b[0],b[-1]-a[0])),a[1:],(a[0][0],a[0][-1],0))[2]

# https://leetcode.com/problems/maximum-distance-in-arrays/discuss/104623/5-liner-C%2B%2B-and-Python-O(m)-simple-solution-O(1)-space

class Solution:
    def maxDistance(self, a: List[List[int]]) -> int:
        res, curMin, curMax = 0, inf, -inf
        for x in a:
            res = max(res, max(x[-1]-curMin, curMax-x[0]))
            curMin, curMax = min(curMin, x[0]), max(curMax, x[-1])
        return res

# https://leetcode.com/problems/maximum-distance-in-arrays/discuss/104658/Short-Python

class Solution:
    def maxDistance(self, a: List[List[int]]) -> int:
        r = range(len(a))
        lo, min_i = min((a[i][0],i) for i in r)
        hi, max_i = max((a[i][-1],i) for i in r)
        return max(max(abs(a[i][0]-hi) for i in r if i != max_i), max(abs(a[i][-1]-lo) for i in r if i != min_i))

class Solution:
    def maxDistance(self, a: List[List[int]]) -> int:
        r = range(len(a))
        g = lambda p,j:p((a[i][j],i) for i in r)
        f = lambda d,j:max(abs(a[i][0]-d) for i in r if i!=j)
        return max(f(*g(min,0)), f(*g(max,-1)))

class Solution:
    def maxDistance(self, a: List[List[int]]) -> int:
        r=range(len(a));f=lambda d,j:max(abs(a[i][0]-d) for i in r if i!=j);g=lambda p,j:f(*p((a[i][j],i) for i in r));return max(g(min,0),g(max,-1))

# https://leetcode.com/problems/maximum-distance-in-arrays/discuss/874566/C%2B%2B-1-liner-and-several-simple-solutions

class Solution:
    def maxDistance(self, n: List[List[int]]) -> int:
        t, a, b = 0, inf, -inf
        for w in n:
            x,y = w[0],w[-1]
            t = max(t, y-a, b-x);
            a,b = min(a,x), max(b,y)
        return t

class Solution:
    def maxDistance(self, n: List[List[int]]) -> int:
        t, x, y = 0, inf, -inf
        for e in n:
            a, b = e[0], e[-1]
            t = max(t, b-x, y-a);
            x,y = min(x,a), max(y,b)
        return t

class Solution:
    def maxDistance(self, n: List[List[int]]) -> int:
        x,y=inf,-inf;return max((a:=w[0],b:=w[-1],max(b-x,y-a),x:=min(x,a),y:=max(y,b))[2]for w in n)

class Solution:
    def maxDistance(self, n: List[List[int]]) -> int:
        x,y=inf,-inf;return max((max(w[-1]-x,y-w[0]),x:=min(x,w[0]),y:=max(y,w[-1]))[0]for w in n)

test('''
624. Maximum Distance in Arrays
Medium

935

79

Add to List

Share
You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.

 

Example 1:

Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Example 2:

Input: arrays = [[1],[1]]
Output: 0
 

Constraints:

m == arrays.length
2 <= m <= 105
1 <= arrays[i].length <= 500
-104 <= arrays[i][j] <= 104
arrays[i] is sorted in ascending order.
There will be at most 105 integers in all the arrays.
Accepted
71,963
Submissions
165,363
''')
