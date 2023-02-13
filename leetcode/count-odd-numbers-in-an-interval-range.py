from lc import *

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1)//2 - low//2

test('''
1523. Count Odd Numbers in an Interval Range
Easy

1580

103

Add to List

Share
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
 

Constraints:

0 <= low <= high <= 10^9
''')

