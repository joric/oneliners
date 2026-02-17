from lc import *

# https://leetcode.com/problems/binary-watch/solutions/1118841/python-one-line-solution-by-mwk0408-fud1/

class Solution:
    def readBinaryWatch(self, t: int) -> List[str]:
        return[f'{i//60}:{i%60:02d}'for i in range(720)if bin(i//60).count('1')+bin(i%60).count('1')==t]

class Solution:
    def readBinaryWatch(self, t: int) -> List[str]:
        return[f'{h}:{m:02}'for h in range(12)for m in range(60)if(h*64+m).bit_count()==t]

class Solution:
    def readBinaryWatch(self, t: int) -> List[str]:
        return[f"{u}:{x%60:02}"for x in range(720)if(x+4*(u:=x//60)).bit_count()==t]

test('''
401. Binary Watch
Easy
Topics
premium lock icon
Companies
Hint
A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

For example, the below binary watch reads "4:51".


Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.

For example, "01:00" is not valid. It should be "1:00".
The minute must consist of two digits and may contain a leading zero.

For example, "10:2" is not valid. It should be "10:02".
 

Example 1:

Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
Example 2:

Input: turnedOn = 9
Output: []
 

Constraints:

0 <= turnedOn <= 10
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
202,302/338.4K
Acceptance Rate
59.8%
Topics
Junior
Backtracking
Bit Manipulation
icon
Companies
Hint 1
Simplify by seeking for solutions that involve comparing bit counts.
Hint 2
Consider calculating all possible times for comparison purposes.
Similar Questions
Letter Combinations of a Phone Number
Medium
Number of 1 Bits
Easy
''')
