from lc import *

# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/discuss/686316/JavaC%2B%2BPython-Binary-Search

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1
        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            flow = bouq = 0
            for a in bloomDay:
                flow = 0 if a > mid else flow + 1
                if flow >= k:
                    flow = 0
                    bouq += 1
                    if bouq == m: break
            if bouq == m:
                right = mid
            else:
                left = mid + 1
        return left


# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/discuss/2233972/Python-oror-6-lines-BinSearch-and-strings-oror-TS%3A-91-97

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def helper(day: int)-> bool:
            return ''.join(['X' if b <= day else ' ' for b in bloomDay]).count('X'*k) >= m
        n, mn, mx = len(bloomDay), min(bloomDay), max(bloomDay)+1
        if n < m * k: return -1
        return mn + bisect_left(range(mn, mx), True, key = helper)

class Solution:
    def minDays(self, b: List[int], m: int, k: int) -> int:
        return m*k>len(b)and -1 or min(b)+bisect_left(range(min(b),max(b)),1,key=lambda d:''.join(('#',' ')[b>d]for b in b).count('#'*k)>=m)

class Solution:
    def minDays(self, b: List[int], m: int, k: int) -> int:
        return m*k<=len(b)and bisect_left(range(max(b)),1,key=lambda d:''.join(('#',' ')[d<x]for x in b).count('#'*k)>=m)or-1

class Solution:
    def minDays(self, b: List[int], m: int, k: int) -> int:
        return b[m*k-1:]and bisect_left(range(10**9),1,key=lambda d:''.join(chr(d<x)for x in b).count('\0'*k)>=m)or-1

test('''
1482. Minimum Number of Days to Make m Bouquets
Medium

3947

132

Add to List

Share
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

 

Example 1:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
Example 2:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
Example 3:

Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here is the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.
 

Other examples:

Input: bloomDay = [97,83], m = 2, k = 1
Output: 97

Constraints:

bloomDay.length == n
1 <= n <= 105
1 <= bloomDay[i] <= 109
1 <= m <= 106
1 <= k <= n
Accepted
150,934
Submissions
286,126
''')
