from lc import *

# https://leetcode.com/problems/water-bottles/discuss/3226806/Python3-or-C%2B%2B-Two-beautiful-solutions

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        drunk, empty = divmod(numBottles, numExchange)
        while drunk:
            result += drunk
            drunk, empty = divmod(empty + drunk, numExchange)
        return result

# https://leetcode.com/problems/water-bottles/discuss/745231/Python-1-liner-with-math-explained

class Solution:
    def numWaterBottles(self, b: int, e: int) -> int:
        return(b*e-1)//(e-1)

class Solution:
    def numWaterBottles(self, b: int, e: int) -> int:
        return b+(b-1)//(e-1)

class Solution:
    def numWaterBottles(self, b: int, e: int) -> int:
        return~-(b*e)//~-e

class Solution:
    def numWaterBottles(self, b: int, e: int) -> int:
        return b+~-b//~-e

class Solution:
    def numWaterBottles(self, b: int, e: int) -> int:
        return~-b//~-e+b

test('''
1518. Water Bottles
Easy

1099

83

Add to List

Share
There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

 

Example 1:


Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.
Example 2:


Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.
 

Constraints:

1 <= numBottles <= 100
2 <= numExchange <= 100
Accepted
91,284
Submissions
145,087
''')