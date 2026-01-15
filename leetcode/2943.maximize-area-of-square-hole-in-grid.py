from lc import *

# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/solutions/4506616/two-lines-solution-by-xxxxkav-b1fa/?envType=daily-question&envId=2026-01-15

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def find_max(bars):
            return max(reduce(lambda w, b: (w[0]+1, w[1]) if b[1]-b[0] == 1 else (2, max(w[0], w[1])), pairwise(sorted(bars)), (2, 0)))
        return min(find_max(hBars), find_max(vBars)) ** 2

# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/solutions/4329556/python-3-5-lines-map-to-strings-ts-98-90-7i53/?envType=daily-question&envId=2026-01-15

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def find_max(bars):
            bars.sort()
            s = ''.join([str(int(y - x == 1)) for x,y in pairwise(bars)])
            return max(map(len,s.split('0')))+2
        return pow(min(find_max(hBars), find_max(vBars)),2)

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, h: List[int], v: List[int]) -> int:
        f=lambda b:max(map(len,''.join(str(int(y-x==1))for x,y in pairwise(sorted(b))).split('0')))+2;return pow(min(f(h),f(v)),2)

# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/solutions/7491818/two-simple-lines-of-code-by-mikposp-jgn8/?envType=daily-question&envId=2026-01-15

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, h: List[int], v: List[int]) -> int:
        return(min(max(accumulate(map(sub,q:=sorted(w),q[1:]),lambda p,x:(x==-1)*-~p,initial=0))for w in(h,v))+2)**2

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, h: List[int], v: List[int]) -> int:
        return(min(max(accumulate([0,*map(sub,q:=sorted(w),q[1:])],lambda p,x:(x==-1)*-~p))for w in(h,v))+2)**2

# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/solutions/4330028/3-lines-python-by-soonwookwon-ala4/?envType=daily-question&envId=2026-01-15

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hgaps = [len(list(v))+1 for _, v in itertools.groupby([h - i for i, h in enumerate(sorted(hBars))])]
        vgaps = [len(list(v))+1 for _, v in itertools.groupby([v - i for i, v in enumerate(sorted(vBars))])]
        return max([min(h, v)**2 for h in hgaps for v in vgaps], default=1)

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, h: List[int], v: List[int]) -> int:
        f=lambda b:max(1+len([*g])for _,g in groupby(x-i for i,x in enumerate(sorted(b))));return pow(min(f(h),f(v)),2)

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, h: List[int], v: List[int]) -> int:
        return min(1+max(len([*g])for _,g in groupby(x-i for i,x in enumerate(sorted(b))))for b in(h,v))**2

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, h: List[int], v: List[int]) -> int:
        return min(1+max(len([*g])for _,g in groupby(starmap(sub,enumerate(sorted(b)))))for b in(h,v))**2

# another solution

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, h: List[int], v: List[int]) -> int:
        return(min(((c:=0)*(l:=-1)+max((c:=(c+1)*(-~l==(l:=x)))for x in sorted(w)))for w in(h,v))+2)**2

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, h: List[int], v: List[int]) -> int:
        return min(1+max(len([*g])for _,g in groupby(map(sub,sorted(b),count())))for b in(h,v))**2

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, h: List[int], v: List[int]) -> int:
        return min(1+max(Counter(starmap(sub,enumerate(sorted(w)))).values())for w in(h,v))**2

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, h: List[int], v: List[int]) -> int:
        return min(1+max(Counter(map(sub,sorted(b),count())).values())for b in(h,v))**2

test('''
2943. Maximize Area of Square Hole in Grid
Medium
Topics
premium lock icon
Companies
Hint
You are given the two integers, n and m and two integer arrays, hBars and vBars. The grid has n + 2 horizontal and m + 2 vertical bars, creating 1 x 1 unit cells. The bars are indexed starting from 1.

You can remove some of the bars in hBars from horizontal bars and some of the bars in vBars from vertical bars. Note that other bars are fixed and cannot be removed.

Return an integer denoting the maximum area of a square-shaped hole in the grid, after removing some bars (possibly none).

 

Example 1:



Input: n = 2, m = 1, hBars = [2,3], vBars = [2]

Output: 4

Explanation:

The left image shows the initial grid formed by the bars. The horizontal bars are [1,2,3,4], and the vertical bars are [1,2,3].

One way to get the maximum square-shaped hole is by removing horizontal bar 2 and vertical bar 2.

Example 2:



Input: n = 1, m = 1, hBars = [2], vBars = [2]

Output: 4

Explanation:

To get the maximum square-shaped hole, we remove horizontal bar 2 and vertical bar 2.

Example 3:



Input: n = 2, m = 3, hBars = [2,3], vBars = [2,4]

Output: 4

Explanation:

One way to get the maximum square-shaped hole is by removing horizontal bar 3, and vertical bar 4.

 

Constraints:

1 <= n <= 109
1 <= m <= 109
1 <= hBars.length <= 100
2 <= hBars[i] <= n + 1
1 <= vBars.length <= 100
2 <= vBars[i] <= m + 1
All values in hBars are distinct.
All values in vBars are distinct.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
21,972/49K
Acceptance Rate
44.8%
Topics
Array
Sorting
Biweekly Contest 118
icon
Companies
Hint 1
Sort hBars and vBars and consider them separately.
Hint 2
Compute the longest sequence of consecutive integer values in each array, denoted as [hx, hy] and [vx, vy], respectively.
Hint 3
The maximum square length we can get is min(hy - hx + 2, vy - vx + 2).
Hint 4
Square the maximum square length to get the area.
Similar Questions
Maximal Square
Medium
Maximum Square Area by Removing Fences From a Field
Medium
''')
