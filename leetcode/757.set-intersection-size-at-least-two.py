from lc import *

# https://leetcode.com/problems/set-intersection-size-at-least-two/solutions/230716/python-5-lines-onlogn-by-jason003-is7e/?envType=daily-question&envId=2025-11-20

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        res, p1, p2 = 0, -float('inf'), -float('inf') # res is the result, p1 and p2 is 2 current points
        for s, e in sorted(intervals, key = lambda i: i[1]): # sort the intervals ascending by their end point
            if s > p2: res, p1, p2 = res + 2, e - 1, e
            elif p1 < s <= p2: res, p1, p2 = res + 1, p2, e
        return res

class Solution:
    def intersectionSizeTwo(self, v: List[List[int]]) -> int:
        r=0;a=b=-inf
        for s,e in sorted(v,key=itemgetter(1)):
            if s>b:
                r,a,b=r+2,e-1,e
            elif a<s<=b:
                r,a,b=r+1,b,e
        return r

class Solution:
    def intersectionSizeTwo(self, v: List[List[int]]) -> int:
        r=0;a=b=-inf
        for s,e in sorted(v,key=itemgetter(1)):
            r,a,b=s>b and(r+2,e-1,e)or a<s<=b and(r+1,b,e)or(r,a,b)
        return r

class Solution:
    def intersectionSizeTwo(self, v: List[List[int]]) -> int:
        p=[0,-inf,-inf];[p:=(f:=lambda r,a,b:s>b and(r+2,e-1,e)or a<s<=b and(r+1,b,e)or(r,a,b))(*p)for s,e in sorted(v,key=itemgetter(1))];return p[0]

# https://leetcode.com/problems/set-intersection-size-at-least-two/solutions/4912570/7-line-simple-on-by-yoongyeom-4uq2/?envType=daily-question&envId=2025-11-20

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[1], -x[0]))
        arr = []
        for s, e in intervals:
            idx = bisect_left(arr, s)
            for i in range(max(2-len(arr)+idx, 0)-1, -1, -1):
                arr.append(e-i)
        return len(arr)

class Solution:
    def intersectionSizeTwo(self, a: List[List[int]]) -> int:
        r=[];[r.extend(e-i for i in reversed(range(max(2-len(r)+bisect_left(r,s),0))))for s,e in sorted(a,key=lambda x:(x[1],-x[0]))];return len(r)

# https://leetcode.com/problems/set-intersection-size-at-least-two/solutions/1050159/java-13-lines-of-code-based-on-sorting-t-rasc/?envType=daily-question&envId=2025-11-20

class Solution:
    def intersectionSizeTwo(self, a: List[List[int]]) -> int:
        a.sort(key=lambda x:(x[1], x[0]))
        r = [a[0][1]-1,a[0][1]]
        for s,e in a[1:]:
            if s > r[-1]:
                r += [e - 1, e]
            elif s > r[-2]:
                r +=[e]
        return len(r)

class Solution:
    def intersectionSizeTwo(self, a: List[List[int]]) -> int:
        a.sort(key=lambda x:(x[1],x[0]));r=[a[0][1]-1,a[0][1]];[r.extend(s>r[-1]and[e-1,e]or s>r[-2]and[e]or[])for s,e in a[1:]];return len(r)

# https://leetcode.com/problems/set-intersection-size-at-least-two/solutions/4457897/python-5-lines-by-dkoshman-abrn/?envType=daily-question&envId=2025-11-20

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        ints = []
        for end, neg_begin in sorted((e, -b) for b, e in intervals):
            n_new = 2 - sum(-neg_begin <= i for i in ints[-2:])
            ints.extend(end - i for i in reversed(range(n_new)))
        return len(ints)

class Solution:
    def intersectionSizeTwo(self, a: List[List[int]]) -> int:
        r=[];[r.extend(e-i for i in reversed(range(2-sum(-b<=i for i in r[-2:]))))for e,b in sorted((e,-b)for b,e in a)];return len(r)

class Solution:
    def intersectionSizeTwo(self, a: List[List[int]]) -> int:
        r=[];[r.extend(e-i for i in range(1-sum(-b<=i for i in r[-2:]),-1,-1))for e,b in sorted((e,-b)for b,e in a)];return len(r)

test('''
757. Set Intersection Size At Least Two
Hard
Topics
premium lock icon
Companies
You are given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.

A containing set is an array nums where each interval from intervals has at least two integers in nums.

For example, if intervals = [[1,3], [3,7], [8,9]], then [1,2,4,7,8,9] and [2,3,4,8,9] are containing sets.
Return the minimum possible size of a containing set.

 

Example 1:

Input: intervals = [[1,3],[3,7],[8,9]]
Output: 5
Explanation: let nums = [2, 3, 4, 8, 9].
It can be shown that there cannot be any containing array of size 4.
Example 2:

Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
Output: 3
Explanation: let nums = [2, 3, 4].
It can be shown that there cannot be any containing array of size 2.
Example 3:

Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
Output: 5
Explanation: let nums = [1, 2, 3, 4, 5].
It can be shown that there cannot be any containing array of size 4.

Other examples:

Input: intervals = [[1,3],[1,2],[0,1]]
Output: 3

Input: intervals = [[2,10],[3,7],[3,15],[4,11],[6,12],[6,16],[7,8],[7,11],[7,15],[11,12]]
Output: 5

Constraints:

1 <= intervals.length <= 3000
intervals[i].length == 2
0 <= starti < endi <= 108
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
30,477/65.1K
Acceptance Rate
46.8%
Topics
Array
Greedy
Sorting
Weekly Contest 65
''')
