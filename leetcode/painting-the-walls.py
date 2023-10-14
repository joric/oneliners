from lc import *

class Solution:
    def paintWalls(self, c: List[int], t: List[int]) -> int:
        return(f:=cache(lambda i,x:x<len(t)and(i<len(c)and min(f(i+1,x),c[i]+f(i+1,x+t[i]+1))or inf)))(0,0)

test('''
2742. Painting the Walls
Hard

504

6

Add to List

Share
You are given two 0-indexed integer arrays, cost and time, of size n representing the costs and the time taken to paint n different walls respectively. There are two painters available:

A paid painter that paints the ith wall in time[i] units of time and takes cost[i] units of money.
A free painter that paints any wall in 1 unit of time at a cost of 0. But the free painter can only be used if the paid painter is already occupied.
Return the minimum amount of money required to paint the n walls.

 

Example 1:

Input: cost = [1,2,3,2], time = [1,2,3,2]
Output: 3
Explanation: The walls at index 0 and 1 will be painted by the paid painter, and it will take 3 units of time; meanwhile, the free painter will paint the walls at index 2 and 3, free of cost in 2 units of time. Thus, the total cost is 1 + 2 = 3.
Example 2:

Input: cost = [2,3,4,2], time = [1,1,1,1]
Output: 4
Explanation: The walls at index 0 and 3 will be painted by the paid painter, and it will take 2 units of time; meanwhile, the free painter will paint the walls at index 1 and 2, free of cost in 2 units of time. Thus, the total cost is 2 + 2 = 4.
 

Constraints:

1 <= cost.length <= 500
cost.length == time.length
1 <= cost[i] <= 10^6
1 <= time[i] <= 500
''')

