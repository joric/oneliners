from lc import *

# https://leetcode.com/problems/image-smoother/discuss/2489901/Python%2B-Numpy

class Solution:
    def imageSmoother(self, m: List[List[int]]) -> List[List[int]]:
        p=__import__('numpy');m=p.array(m,dtype=float);a=p.pad(m,((1,1),(1,1)),mode='constant',constant_values=(p.nan,));return[[int(p.nansum(a[i-1:i+2,j-1:j+2])/p.count_nonzero(~p.isnan(a[i-1:i+2,j-1:j+2])))for j in range(1,m.shape[1]+1)]for i in range(1,m.shape[0]+1)]

# https://leetcode.com/problems/image-smoother/discuss/625175/Python3-One-line-for-fun-(beats-49.81)

class Solution:
    def imageSmoother(self, m: List[List[int]]) -> List[List[int]]:
        h,w=len(m),len(m[0]);return [[(sum([sum(_[max(0,j-1):min(w,j+2)])for _ in m[max(0,i-1):min(h,i+2)]]))//((min(h,i+2)-max(0,i-1))*(min(w,j+2)-max(0,j-1)))for j in range(w)]for i in range(h)]

# https://leetcode.com/problems/image-smoother/discuss/566866/Python-3-one-line

class Solution:
    def imageSmoother(self, m: List[List[int]]) -> List[List[int]]:
        h,w=len(m),len(m[0]);return[[int(mean(m[i][j]for i in(y-1,y,y+1)for j in(x-1,x,x+1)if w>j>=0<=i<h))for x in range(w)]for y in range(h)]

test('''
661. Image Smoother
Easy

750

2373

Add to List

Share
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).


Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.

 

Example 1:


Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Example 2:


Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
 

Constraints:

m == img.length
n == img[i].length
1 <= m, n <= 200
0 <= img[i][j] <= 255
Accepted
105,339
Submissions
170,927
''')
