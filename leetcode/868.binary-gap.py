from lc import *

# https://leetcode.com/problems/binary-gap/solutions/151143/python-1-line-solution/

class Solution:
    def binaryGap(self, n: int) -> int:
        return max(len(c)for c in bin(n)[2:].strip('0').split('1'))+bool(n&(n-1))

# https://leetcode.com/problems/binary-gap/solutions/4204563/python-3-best-one-line/

class Solution:
    def binaryGap(self, n: int) -> int:
        return max([*map(lambda x:len(x)+1,bin(n)[2:].split('1')[1:-1]),0])

class Solution:
    def binaryGap(self, n: int) -> int:
        return max([0]+[1+len(x)for x in bin(n)[2:].split('1')[1:-1]])

test('''
868. Binary Gap
Easy
Topics
Companies
Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.

 

Example 1:

Input: n = 22
Output: 2
Explanation: 22 in binary is "10110".
The first adjacent pair of 1's is "10110" with a distance of 2.
The second adjacent pair of 1's is "10110" with a distance of 1.
The answer is the largest of these two distances, which is 2.
Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.
Example 2:

Input: n = 8
Output: 0
Explanation: 8 in binary is "1000".
There are not any adjacent pairs of 1's in the binary representation of 8, so we return 0.
Example 3:

Input: n = 5
Output: 2
Explanation: 5 in binary is "101".
 

Constraints:

1 <= n <= 109
Seen this question in a real interview before?
1/5
Yes
No
Accepted
90.8K
Submissions
141.3K
Acceptance Rate
64.3%
Topics
Bit Manipulation
''')

