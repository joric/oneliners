from lc import *

class Solution:
    def integerBreak(self, n: int) -> int:
        return(3**((n-2)//3)*(n-((n-2)//3)*3),n-1)[n<4]

test('''
343. Integer Break
Medium

3916

374

Add to List

Share
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 

Example 3:

Input: n = 5
Output: 6


Constraints:

2 <= n <= 58
''')

