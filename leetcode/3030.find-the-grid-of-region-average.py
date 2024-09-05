from lc import *

# weekly-contest-383 Q3
# https://leetcode.com/contest/weekly-contest-383
# https://leetcode.com/problems/find-the-grid-of-region-average

# numpy version

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        import numpy as np
        import scipy
        img = np.array(image)
        m, n = img.shape
        dx = np.abs(img[1:] - img[:-1])
        dy = np.abs(img[:, 1:] - img[:, :-1])
        dall = []
        for i in range(3):
            dall += [dx[1:, i:n - 2 + i], dx[:-1, i:n - 2 + i], dy[i:m - 2 + i, 1:], dy[i:m - 2 + i, :-1]]
        mask = np.max(dall, axis=0) <= threshold
        avg = (scipy.signal.convolve2d(img, np.ones((3, 3)) / 9, 'valid') + 1e-8).astype(int)
        eff = mask * avg
        ans =  np.zeros_like(img)
        mans = np.zeros_like(img)
        for i in range(3):
            for j in range(3):
                ans[i:m - 2 + i, j:n - 2 + j] += eff
                mans[i:m - 2 + i, j:n - 2 + j] += mask
        result = ans / mans
        na = np.isnan(result)
        result[na] = img[na]
        return (result + 1e-8).astype(int)

class Solution:
    def resultGrid(self, a: List[List[int]], t: int) -> List[List[int]]:
        p,s=map(__import__,('numpy','scipy'))
        g=p.array(a)
        m,n=g.shape
        x,y=p.abs(g[1:]-g[:-1]),p.abs(g[:,1:]-g[:,:-1])
        d=sum(([x[1:,i:n-2+i],x[:-1,i:n-2+i],y[i:m-2+i,1:],y[i:m-2+i,:-1]]for i in(0,1,2)),start=[])
        k=p.max(d,axis=0)<=t
        v=(s.signal.convolve2d(g,p.ones((3,3))/9,'valid')+1e-8).astype(int)
        f=k*v
        w=p.zeros_like(g)
        z=p.zeros_like(g)
        for i in range(3):
            for j in range(3):
                w[i:m-2+i,j:n-2+j]+=f
                z[i:m-2+i,j:n-2+j]+=k
        r=w/z
        b=p.isnan(r)
        r[b]=g[b]
        return(r+1e-8).astype(int)

# https://leetcode.com/problems/find-the-grid-of-region-average/discuss/4674240/Simple-Explained-oror-Python

class Solution:
    def resultGrid(self, p: List[List[int]], t: int) -> List[List[int]]:
        h = len(p)
        w = len(p[0])
        r = [[[0,0]]*w for _ in range(h)]
        for y in range(h-2):
            for x in range(w-2):
                c = 0
                b = True
                for i in range(y,y+3):
                    for j in range(x,x+3):
                        if (i-1 >= y and abs(p[i-1][j] - p[i][j]) > t) or (j-1 >= x and abs(p[i][j-1] - p[i][j]) > t):
                            b = False
                            break
                        c += p[i][j]
                    if b==False:
                        break
                if b:
                    c = c // 9
                    for i in range(y,y+3):
                        for j in range(x,x+3):
                            r[i][j] = [r[i][j][0]+c,r[i][j][1]+1]
        for y in range(h):
            for x in range(w):
                if r[y][x][1] == 0:
                    r[y][x] = p[y][x]
                else:
                    r[y][x] = r[y][x][0] // r[y][x][1]
        return r

class Solution:
    def resultGrid(self, p: List[List[int]], t: int) -> List[List[int]]:
        h,w,e = len(p), len(p[0]), enumerate
        r = [[[0,0]]*w for _ in range(h)]
        def f(y,x,c=0):
            for i in range(y,y+3):
                for j in range(x,x+3):
                    if (i-1>=y and abs(p[i-1][j]-p[i][j])>t)or(j-1>=x and abs(p[i][j-1]-p[i][j])>t):
                        return 0,c
                    c += p[i][j]
            return 1,c
        for y in range(h-2):
            for x in range(w-2):
                b,c = f(y,x)
                b and[setitem(r[i],j,[r[i][j][0]+c//9,r[i][j][1]+1])for j in range(x,x+3)for i in range(y,y+3)]
        return[[p[i][j]if 1>v[1]else v[0]//v[1] for j,v in e(t)]for i,t in e(r)]

class Solution:
    def resultGrid(self, p: List[List[int]], t: int) -> List[List[int]]:
        h,w,e,g=len(p),len(p[0]),enumerate,range;r=[[[0,0]]*w for _ in g(h)];f=lambda y,x,c=0:(not any((i-1>=y and abs(p[i-1][j]-p[i][j])>t)or(j-1>=x and abs(p[i][j-1]-p[i][j])>t)or not[c:=c+p[i][j]]for i in g(y,y+3)for j in g(x,x+3)),c);[(k:=f(y,x))[0]and[setitem(r[i],j,[r[i][j][0]+k[1]//9,r[i][j][1]+1])for j in g(x,x+3)for i in g(y,y+3)]for y in g(h-2)for x in g(w-2)];return[[p[i][j]if 1>v[1]else v[0]//v[1]for j,v in e(t)]for i,t in e(r)]

test('''
3030. Find the Grid of Region Average
Medium

10

42

Add to List

Share
You are given a 0-indexed m x n grid image which represents a grayscale image, where image[i][j] represents a pixel with intensity in the range[0..255]. You are also given a non-negative integer t.

Two pixels image[a][b] and image[c][d] are said to be adjacent if |a - c| + |b - d| == 1.

A region is a 3 x 3 subgrid where the absolute difference in intensity between any two adjacent pixels is less than or equal to threshold.

All pixels in a region belong to that region, note that a pixel can belong to multiple regions.

You need to calculate a 0-indexed m x n grid result, where result[i][j] is the average intensity of the region to which image[i][j] belongs, rounded down to the nearest integer. If image[i][j] belongs to multiple regions, result[i][j] is the average of the rounded down average intensities of these regions, rounded down to the nearest integer. If image[i][j] does not belong to any region, result[i][j] is equal to image[i][j].

Return the grid result.

 

Example 1:


Input: image = [[5,6,7,10],[8,9,10,10],[11,12,13,10]], threshold = 3
Output: [[9,9,9,9],[9,9,9,9],[9,9,9,9]]
Explanation: There exist two regions in the image, which are shown as the shaded areas in the picture. The average intensity of the first region is 9, while the average intensity of the second region is 9.67 which is rounded down to 9. The average intensity of both of the regions is (9 + 9) / 2 = 9. As all the pixels belong to either region 1, region 2, or both of them, the intensity of every pixel in the result is 9. 
Please note that the rounded-down values are used when calculating the average of multiple regions, hence the calculation is done using 9 as the average intensity of region 2, not 9.67.
Example 2:


Input: image = [[10,20,30],[15,25,35],[20,30,40],[25,35,45]], threshold = 12
Output: [[25,25,25],[27,27,27],[27,27,27],[30,30,30]]
Explanation: There exist two regions in the image, which are shown as the shaded areas in the picture. The average intensity of the first region is 25, while the average intensity of the second region is 30. The average intensity of both of the regions is (25 + 30) / 2 = 27.5 which is rounded down to 27. All the pixels in row 0 of the image belong to region 1, hence all the pixels in row 0 in the result are 25. Similarly, all the pixels in row 3 in the result are 30. The pixels in rows 1 and 2 of the image belong to region 1 and region 2, hence their assigned value is 27 in the result.
Example 3:

Input: image = [[5,6,7],[8,9,10],[11,12,13]], threshold = 1
Output: [[5,6,7],[8,9,10],[11,12,13]]
Explanation: There does not exist any region in image, hence result[i][j] == image[i][j] for all the pixels.


Example 4:

Input: image = [[0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],[4,4,4,4,4,4,5,4,4,4,4,11,4,8,4,4,4,11,4,4,4,4,4,4,4],[0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],[4,4,4,4,4,4,5,4,4,4,4,11,4,8,4,4,4,11,4,4,4,4,4,4,4],[9,9,9,9,9,9,10,9,9,9,9,16,9,13,9,9,9,16,9,9,9,9,9,9,9],[0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],[5,5,5,5,5,5,6,5,5,5,5,12,5,9,5,5,5,12,5,5,5,5,5,5,5],[16,16,16,16,16,16,17,16,16,16,16,23,16,20,16,16,16,23,16,16,16,16,16,16,16],[0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],[8,8,8,8,8,8,9,8,8,8,8,15,8,12,8,8,8,15,8,8,8,8,8,8,8],[0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],[1,1,1,1,1,1,2,1,1,1,1,8,1,5,1,1,1,8,1,1,1,1,1,1,1],[0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,7,0,4,0,0,0,7,0,0,0,0,0,0,0]], threshold = 41
Output: [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 1, 2, 2, 3, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 1, 2, 2, 3, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 1, 2, 2, 3, 2, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 2, 1, 1, 2, 2, 2, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 1, 1, 1, 2, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 1, 1, 1, 2, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 3, 3, 2, 2, 3, 3, 3, 2, 1, 1, 1, 1, 1], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 5, 5, 3, 4, 4, 5, 4, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 6, 6, 4, 5, 5, 6, 5, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 7, 7, 5, 6, 6, 7, 6, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 8, 8, 6, 7, 7, 8, 7, 6, 6, 6, 6, 6, 6], [6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 8, 8, 8, 7, 7, 7, 8, 7, 7, 6, 6, 6, 6, 6], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 6, 5, 4, 5, 5, 6, 5, 4, 4, 4, 4, 4, 4], [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 3, 3, 2, 2, 3, 3, 3, 2, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 2, 3, 3, 2, 1, 1, 2, 3, 2, 1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 3, 4, 4, 3, 2, 2, 3, 4, 3, 2, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 3, 2, 2, 3, 4, 5, 5, 4, 3, 3, 4, 5, 4, 3, 2, 2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 3, 4, 4, 3, 2, 2, 3, 4, 3, 2, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 2, 1, 2, 2, 3, 2, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0]]

Constraints:

3 <= n, m <= 500
0 <= image[i][j] <= 255
0 <= threshold <= 255
Accepted
4,840
Submissions
12,206
''')