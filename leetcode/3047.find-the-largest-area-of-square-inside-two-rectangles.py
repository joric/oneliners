from lc import *

# Q2. https://leetcode.com/contest/weekly-contest-386/problems/find-the-largest-area-of-square-inside-two-rectangles/
# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles

# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/discuss/4779287/easy-solution-in-python

class Solution:
    def largestSquareArea(self, a: List[List[int]], b: List[List[int]]) -> int:
        n=len(a)
        r = 0
        for i in range(n):
            for j in range(i+1,n):
                w = max(0,min(b[i][0],b[j][0])-max(a[i][0],a[j][0]))
                h = max(0,min(b[i][1],b[j][1])-max(a[i][1],a[j][1]))
                r = max(r,min(w,h)**2)
        return r

class Solution:
    def largestSquareArea(self, a: List[List[int]], b: List[List[int]]) -> int:
        n=len(a);return max(min(max(0,min(b[i][0],b[j][0])-max(a[i][0],a[j][0])),max(0,min(b[i][1],b[j][1])-max(a[i][1],a[j][1])))**2 for i in range(n)for j in range(i+1,n))

# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/discuss/4779237/Python-3-oror-8-lines-iteration-oror-TS%3A-3813-ms-17-MB

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        r = 0
        for((a,b),(c,d)),((e,f),(g,h))in combinations(zip(bottomLeft,topRight),2):
            r = max(r, min(min(c,g)-max(a,e),min(d,h)-max(b,f)))
        return r**2

class Solution:
    def largestSquareArea(self, p: List[List[int]], q: List[List[int]]) -> int:
        return max(max(0,min(min(c,g)-max(a,e),min(d,h)-max(b,f)))for((a,b),(c,d)),((e,f),(g,h))in combinations(zip(p,q),2))**2

class Solution:
    def largestSquareArea(self, p: List[List[int]], q: List[List[int]]) -> int:
        return(m:=max)(m(0,min(min(c,g)-m(a,e),min(d,h)-m(b,f)))for((a,b),(c,d)),((e,f),(g,h))in combinations(zip(p,q),2))**2

test('''
3047. Find the Largest Area of Square Inside Two Rectangles
User Accepted:8669
User Tried:11005
Total Accepted:9290
Total Submissions:22576
Difficulty:Medium
There exist n rectangles in a 2D plane. You are given two 0-indexed 2D integer arrays bottomLeft and topRight, both of size n x 2, where bottomLeft[i] and topRight[i] represent the bottom-left and top-right coordinates of the ith rectangle respectively.

You can select a region formed from the intersection of two of the given rectangles. You need to find the largest area of a square that can fit inside this region if you select the region optimally.

Return the largest possible area of a square, or 0 if there do not exist any intersecting regions between the rectangles.

 

Example 1:


Input: bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]
Output: 1
Explanation: A square with side length 1 can fit inside either the intersecting region of rectangle 0 and rectangle 1, or the intersecting region of rectangle 1 and rectangle 2. Hence the largest area is side * side which is 1 * 1 == 1.
It can be shown that a square with a greater side length can not fit inside any intersecting region.
Example 2:


Input: bottomLeft = [[1,1],[2,2],[1,2]], topRight = [[3,3],[4,4],[3,4]]
Output: 1
Explanation: A square with side length 1 can fit inside either the intersecting region of rectangle 0 and rectangle 1, the intersecting region of rectangle 1 and rectangle 2, or the intersection region of all 3 rectangles. Hence the largest area is side * side which is 1 * 1 == 1.
It can be shown that a square with a greater side length can not fit inside any intersecting region.
Note that the region can be formed by the intersection of more than 2 rectangles.
Example 3:


Input: bottomLeft = [[1,1],[3,3],[3,1]], topRight = [[2,2],[4,4],[4,2]]
Output: 0
Explanation: No pair of rectangles intersect, hence, we return 0.
 

Other examples:

Input: bottomLeft = [[2,2],[3,1]], topRight = [[5,5],[5,5]]
Output: 4

Constraints:

n == bottomLeft.length == topRight.length
2 <= n <= 103
bottomLeft[i].length == topRight[i].length == 2
1 <= bottomLeft[i][0], bottomLeft[i][1] <= 107
1 <= topRight[i][0], topRight[i][1] <= 107
bottomLeft[i][0] < topRight[i][0]
bottomLeft[i][1] < topRight[i][1]
''')