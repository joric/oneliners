from lc import *

# https://leetcode.com/problems/water-bottles-ii/solutions/5012105/python3-two-lines-beat-99-o-numbottles-numexchange/?envType=daily-question&envId=2025-10-02

class Solution:
    def maxBottlesDrunk(self, b: int, e: int) -> int:
        d = b
        while b>=e:
            b -= e
            b += 1
            d += 1
            e += 1
        return d

class Solution:
    def maxBottlesDrunk(self,b:int,e:int)->int:
        r=0
        while b>=e:
            r+=e
            b=b-e+1
            e+=1
        return r+b

class Solution:
    def maxBottlesDrunk(self, b: int, e: int) -> int:
        return(f:=lambda b,e:b<e and b or f(b-e+1,e+1)+e)(b,e)

class Solution:
    def maxBottlesDrunk(self, b: int, e: int) -> int:
        return b<e and b or self.maxBottlesDrunk(b-e+1,e+1)+e

test('''
3100. Water Bottles II
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given two integers numBottles and numExchange.

numBottles represents the number of full water bottles that you initially have. In one operation, you can perform one of the following operations:

Drink any number of full water bottles turning them into empty bottles.
Exchange numExchange empty bottles with one full water bottle. Then, increase numExchange by one.
Note that you cannot exchange multiple batches of empty bottles for the same value of numExchange. For example, if numBottles == 3 and numExchange == 1, you cannot exchange 3 empty water bottles for 3 full bottles.

Return the maximum number of water bottles you can drink.

 

Example 1:


Input: numBottles = 13, numExchange = 6
Output: 15
Explanation: The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.
Example 2:


Input: numBottles = 10, numExchange = 3
Output: 13
Explanation: The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.
 

Constraints:

1 <= numBottles <= 100 
1 <= numExchange <= 100
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
42,033/66.3K
Acceptance Rate
63.4%
Topics
Math
Simulation
Weekly Contest 391
icon
Companies
Hint 1
Simulate the process step by step. At each step, drink numExchange bottles of water then exchange them for a full bottle. Keep repeating this step until you cannot exchange bottles anymore.
Similar Questions
Water Bottles
Easy
''')
