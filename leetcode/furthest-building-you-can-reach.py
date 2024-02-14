from lc import *

# Q3. https://leetcode.com/contest/weekly-contest-213/
# https://leetcode.com/problems/furthest-building-you-can-reach/

# my greedy solution (disqualified postfactum) passes tests 1-3

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        for i in range(1, n):
            diff = heights[i] - heights[i-1]
            if diff <= 0:
                continue
            if diff <= bricks:
                bricks -= diff
            elif ladders > 0:
                ladders -= 1
            else:
                return i-1
        return n-1

# https://leetcode.com/problems/furthest-building-you-can-reach/discuss/918515/JavaC%2B%2BPython-Priority-Queue
# note recursive solutions cause MLE on newer tests

class Solution:
    def furthestBuilding(self, h: List[int], b: int, l: int) -> int:
        q = []
        for i in range(len(h) - 1):
            d = h[i+1] - h[i]
            if d > 0:
                heappush(q, d)
            if len(q) > l:
                b -= heappop(q)
            if b < 0:
                return i
        return len(h) - 1

class Solution:
    def furthestBuilding(self, h: List[int], b: int, l: int) -> int:
        q = []
        for i in range(len(h)-1):
            (d:=h[i+1]-h[i],d>0 and heappush(q,d),len(q)>l and (b:=b-heappop(q)))
            if b<0:
                return i
        return len(h) - 1

class Solution:
    def furthestBuilding(self, h: List[int], b: int, l: int) -> int:
        return next((i for i in range(len(h)-1) if not(d:=h[i+1]-h[i],d>0 and heappush(q,d),l<len(q)and(b:=b-heappop(q)))or b<0),(q:=[])or len(h)-1)

test('''
1642. Furthest Building You Can Reach
Medium

4543

95

Add to List

Share
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

 

Example 1:


Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
Example 2:

Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7
Example 3:

Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3
 

Example 4:

Input: heights = [1,5,1,2,3,4,10000], bricks = 4, ladders = 1
Output: 5

Constraints:

1 <= heights.length <= 105
1 <= heights[i] <= 106
0 <= bricks <= 109
0 <= ladders <= heights.length
Accepted
124,786
Submissions
257,374
''')
