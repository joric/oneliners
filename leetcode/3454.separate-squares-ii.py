from lc import *

# https://leetcode.com/problems/separate-squares-ii/solutions/7492569/python-not-binary-consume-rectangles-500-tdkk/?envType=daily-question&envId=2026-01-14

class Solution:
    def separateSquares(self, a: List[List[int]]) -> float:
        e = defaultdict(list)
        for l, d, s in a:
            e[d].append((1, l, l + s))
            e[d + s].append((0, l, l + s))
        c = []; g = 0; k = []
        for y, n in pairwise(sorted(e)):
            for p, a, b in e[y]:
                if p:
                    insort_left(c, (a, b))
                else:
                    c.remove((a, b))
            w = 0
            l = 0
            for a, b in c:
                if a >= l:
                    w += b - a
                    l = b
                elif b > l:
                    w += b - l
                    l = b
            g += (n - y) * w
            k.append((n,w,g))
        for x in k:
            if x[2] >= g/2:
                return x[0] - (x[2] - g/2) / x[1]

class Solution:
    def separateSquares(self, a: List[List[int]]) -> float:
        g=0;e=defaultdict(list);c=[];k=[];[e[d].append((1,l,l+s))or e[d+s].append((0,l,l+s))for l,d,s in a];[([insort_left(c,(a,b))if p else c.remove((a,b))for p,a,b in e[y]],w:=0,l:=0,[a>=l and(w:=w+b-a,l:=b)or b>l and(w:=w+b-l,l:=b)for a,b in c],g:=g+(n-y)*w,k.append((n,w,g)))for y,n in pairwise(sorted(e))];return next(x[0]-(x[2]-g/2)/x[1]for x in k if x[2]>=g/2)

class Solution:
    def separateSquares(self, a: List[List[int]]) -> float:
        e={};c=[];k=[];g=0;
        for l,d,s in a:
            for i,t in((1,d),(0,d+s)):
                e.setdefault(t,[]).append((i,l,l+s))
        for y,n in pairwise(sorted(e)):
            for i,*x in e[y]:
                c.append(x)if i else c.remove(x)
            u=w=0
            for x,v in sorted(c):
                u<v and(w:=w+v-max(u,x),u:=v)
            k.append((g:=g+(n-y)*w,w,n))
        return next(n-(t-g/2)/w for t,w,n in k if t>=g/2)

class Solution:
    def separateSquares(self, a: List[List[int]]) -> float:
        e,c,g={},[],0;[e.setdefault(t,[]).append((i,l,l+s))for l,d,s in a for i,t in((1,d),(0,d+s))];q=[(w,n-y,n)for y,n in pairwise(sorted(e))if([c.append(x)if i else c.remove(x)for i,*x in e[y]],u:=0,w:=0,[u<v and(w:=w+v-max(u,x),u:=v)for x,v in sorted(c)])];t=sum(w*h for w,h,_ in q)/2;return next(n-(g-t)/w for w,h,n in q if(g:=g+w*h)>=t)

class Solution:
    def separateSquares(self, a: List[List[int]]) -> float:
        e={};c=[];k=[];g=0;[e.setdefault(t,[]).append((i,l,l+s))for l,d,s in a for i,t in((1,d),(0,d+s))];[([c.append(x)if i else c.remove(x)for i,*x in e[y]],u:=0,w:=0,[u<v and(w:=w+v-max(u,x),u:=v)for x,v in sorted(c)],k.append((g:=g+(n-y)*w,w,n)))for y,n in pairwise(sorted(e))];return next(n-(t-g/2)/w for t,w,n in k if t>=g/2)

class Solution:
    def separateSquares(self, a: List[List[int]]) -> float:
        e,c,k,g={},[],[],0;[(e.setdefault(d+s*j,[]).append((1-j,l,l+s)))for l,d,s in a for j in(0,1)];[([[c.remove,c.append][i](x)for i,*x in e[y]],u:=0,w:=0,[u<v and(w:=w+v-max(u,x),u:=v)for x,v in sorted(c)],k.append((g:=g+(n-y)*w,w,n)))for y,n in pairwise(sorted(e))];return next(n-(t-g/2)/w for t,w,n in k if t>=g/2)

test('''
3454. Separate Squares II
Hard
Topics
premium lock icon
Companies
Hint
You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Find the minimum y-coordinate value of a horizontal line such that the total area covered by squares above the line equals the total area covered by squares below the line.

Answers within 10-5 of the actual answer will be accepted.

Note: Squares may overlap. Overlapping areas should be counted only once in this version.

 

Example 1:

Input: squares = [[0,0,1],[2,2,1]]

Output: 1.00000

Explanation:



Any horizontal line between y = 1 and y = 2 results in an equal split, with 1 square unit above and 1 square unit below. The minimum y-value is 1.

Example 2:

Input: squares = [[0,0,2],[1,1,1]]

Output: 1.00000

Explanation:



Since the blue square overlaps with the red square, it will not be counted again. Thus, the line y = 1 splits the squares into two equal parts.

Other examples:

Input: squares = [[5,18,12],[7,23,3],[7,25,7]]
Output: 24.58333

Constraints:

1 <= squares.length <= 5 * 104
squares[i] = [xi, yi, li]
squares[i].length == 3
0 <= xi, yi <= 109
1 <= li <= 109
The total area of all the squares will not exceed 1015.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
11,333/25.5K
Acceptance Rate
44.4%
Topics
Array
Binary Search
Segment Tree
Line Sweep
Biweekly Contest 150
icon
Companies
Hint 1
Use a line sweep and a segment tree.
Hint 2
The line must lie in one of the squares.
Similar Questions
Rectangle Area II
Hard
''')
