from lc import *

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l, r = 1, m*n
        while l < r: 
            x = l + r >> 1
            s = sum(min(n, x//(i+1)) for i in range(m))
            if s < k:
                l = x + 1
            else:
                r = x
        return l

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        return bisect_left(range(n*m),0,key=lambda x:sum(min(n,x//(i+1)) for i in range(m))-k)

test('''

668. Kth Smallest Number in Multiplication Table
Hard

Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.

Example 1:

Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The 5th smallest number is 3.

Example 2:

Input: m = 2, n = 3, k = 6
Output: 6
Explanation: The 6th smallest number is 6.

Constraints:

1 <= m, n <= 3 * 10^4
1 <= k <= m * n

''')
