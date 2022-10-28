from lc import *

# https://leetcode.com/problems/image-overlap/discuss/832150/Python-2-lines-using-convolutions-explained

from scipy.ndimage import convolve
import numpy as np

class Solution1:
    def largestOverlap(self, A, B):
        B = np.pad(B, len(A), mode='constant', constant_values=(0, 0))
        return np.amax(convolve(B, np.flip(np.flip(A,1),0), mode='constant'))

# https://leetcode.com/problems/image-overlap/discuss/199638/Python-using-Fast-Fourier-Transform-O(N2-log-N)

import numpy as np

class Solution2:
    def largestOverlap(self, A, B):
        n = len(A)
        A1 = np.pad(A, [(0, n), (0, n)], mode='constant', constant_values=0)
        B1 = np.pad(B, [(0, n), (0, n)], mode='constant', constant_values=0)
        A2 = np.fft.fft2(A1)
        B2 = np.fft.ifft2(B1)
        return int(np.round(np.max(np.abs(np.fft.fft2(A2 * B2)))))

# https://leetcode.com/problems/image-overlap/discuss/832472/Python-by-offset-vector-counting-w-Comment

class Solution3:
    def largestOverlap(self, A, B):
        N = len(A)
        pos_of_1_in_A = [(xi, yi) for xi in range(N) for yi in range(N) if A[xi][yi]]
        pos_of_1_in_B = [(xi, yi) for xi in range(N) for yi in range(N) if B[xi][yi]]
        offset_vector_counting = Counter([(x1 - x2, y1 - y2) for (x1, y1) in pos_of_1_in_A for (x2, y2) in pos_of_1_in_B ])
        return max(offset_vector_counting.values() or [0])

class Solution4:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        return (f:=lambda v:(n:=len(v)) and [(i,j) for i in range(n) for j in range(n) if v[i][j]],
            a:=f(img1), b:=f(img2)) and max(Counter([(x1-x2, y1-y2) for (x1,y1) in a for (x2,y2) in b]).values() or [0])

# https://leetcode.com/problems/image-overlap/discuss/130623/C%2B%2BJavaPython-Straight-Forward

class Solution5:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        a = [i // n * 50 + i % n for i in range(n * n) if img1[i // n][i % n]]
        b = [i // n * 50 + i % n for i in range(n * n) if img2[i // n][i % n]]
        return max(Counter(i - j for i in a for j in b).values() or [0])

class Solution6:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        return (f:=lambda v:(n:=len(v)) and [i//n*50+i%n for i in range(n*n) if v[i//n][i%n]],
            a:=f(img1), b:=f(img2)) and max(Counter(i-j for i in a for j in b).values() or [0])

class Solution(object):
    def largestOverlap(self, a, b):
        return (f:=lambda v:(n:=len(v)) and [i//n*50+i%n for i in range(n*n)
            if v[i//n][i%n]]) and max(Counter(i-j for i in f(a) for j in f(b)).values() or [0])


test('''
835. Image Overlap
Medium

588

182

Add to List

Share
You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.

 

Example 1:


Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3 (shown in red).

Example 2:

Input: img1 = [[1]], img2 = [[1]]
Output: 1
Example 3:

Input: img1 = [[0]], img2 = [[0]]
Output: 0
 

Constraints:

n == img1.length == img1[i].length
n == img2.length == img2[i].length
1 <= n <= 30
img1[i][j] is either 0 or 1.
img2[i][j] is either 0 or 1.
''')
