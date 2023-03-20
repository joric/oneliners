from lc import *

class Solution:
    def canPlaceFlowers(self, d: List[int], n: int) -> bool:
        m = len(d)
        for i in range(m):
            c = d[i]==0 and (i==0 or d[i-1]==0) and (i==m-1 or d[i+1]==0)
            if c:
                d[i] = 1
                n -= 1
        return n<=0

class Solution:
    def canPlaceFlowers(self, d: List[int], n: int) -> bool:
        return n<=sum((len([*g])-1)//2 for t,g in groupby([0]+d+[0]) if t==0)

test('''

605. Can Place Flowers
Easy

3594

727

Add to List

Share
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 10^4
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

Accepted
348,723
Submissions
1,074,896

''')
