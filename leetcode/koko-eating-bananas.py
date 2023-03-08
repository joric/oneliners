from lc import *

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = (l + r)//2
            if sum((p+m-1)//m for p in piles)>h:
                l = m + 1
            else:
                r = m
        return l

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = (l + r)//2
            if sum(ceil(p/m) for p in piles)>h:
                l = m + 1
            else:
                r = m
        return l

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return bisect_left(type('',(),{'__getitem__':lambda _,m:sum(ceil(p/m) for p in piles)<=h})(),True,1,max(piles))

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return bisect_left(range(1,max(piles)),-h,key=lambda m:-sum((p+m-1)//m for p in piles))+1

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return bisect_left(range(1,max(piles)),1,key=lambda m:sum(ceil(p/m) for p in piles)<=h)+1

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return bisect_left(range(1,max(piles)),-h,key=lambda m:-sum(ceil(p/m) for p in piles))+1

test('''
875. Koko Eating Bananas
Medium

6151

298

Add to List

Share
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Example 4:
Input: piles = [312884470], h = 968709470
Output: 1

Constraints:

1 <= piles.length <= 10^4
piles.length <= h <= 10^9
1 <= piles[i] <= 10^9
''')

