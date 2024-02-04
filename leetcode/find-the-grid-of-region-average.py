from lc import *

# weekly-contest-383 Q3
# https://leetcode.com/problems/find-the-grid-of-region-average/discuss/4674240/Simple-Explained-oror-Python3

class Solution:
    def resultGrid(self, p: List[List[int]], t: int) -> List[List[int]]:
        h,w = len(p), len(p[0])
        r = [[[0,0]]*w for _ in range(h)]
        for y in range(h-2):
            for x in range(w-2):
                c = 0
                f = True
                for i in range(y,y+3):
                    for j in range(x,x+3):
                        if (i-1 >= y and abs(p[i-1][j] - p[i][j]) > t) or (j-1 >= x and abs(p[i][j-1] - p[i][j]) > t):
                            f = False
                            break
                        c += p[i][j]
                    if not f:
                        break
                f and [setitem(r[i],j,[r[i][j][0]+c//9,r[i][j][1]+1])for j in range(x,x+3)for i in range(y,y+3)]
        return[[r[y][x][1]and r[y][x][0]//r[y][x][1]or p[y][x] for x in range(w)]for y in range(h)]

# TODO

test('''
3030. Find the Grid of Region Average
Medium

10

42

Add to List

Share
You are given a 0-indexed m x n grid image which represents a grayscale image, where image[i][j] represents a pixel with intensity in the range[0..255]. You are also given a non-negative integer threshold.

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
 

Constraints:

3 <= n, m <= 500
0 <= image[i][j] <= 255
0 <= threshold <= 255
Accepted
4,840
Submissions
12,206
''')


