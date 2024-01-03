from lc import *

# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/discuss/2272999/PYTHON-3-99.13-LESS-MEMORY-or-94.93-FASTER-or-EXPLANATION

class Solution:
    def numberOfBeams(self, b: List[str]) -> int:
        b=[c for s in b if(c:=s.count('1'))];return sum(map(mul,b[1:],b))

# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/discuss/1660943/Python3-Java-C%2B%2B-Simple-O(mn)

class Solution:
    def numberOfBeams(self, b: List[str]) -> int:
        r = p = 0
        for s in b:
            c = s.count('1')
            if c:
                r += p * c
                p = c
        return r

class Solution:
    def numberOfBeams(self, b: List[str]) -> int:
        return reduce(lambda p,s:(c:=s.count('1'))and(p[0]+p[1]*c,c)or p,b,(0,0))[0]

class Solution:
    def numberOfBeams(self, b: List[str]) -> int:
        r=p=0;[(c:=s.count('1'))and(r:=r+p*c,p:=c)for s in b];return r

test('''
2125. Number of Laser Beams in a Bank
Medium

860

76

Add to List

Share
Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.

There is one laser beam between any two security devices if both conditions are met:

The two devices are located on two different rows: r1 and r2, where r1 < r2.
For each row i where r1 < i < r2, there are no security devices in the ith row.
Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return the total number of laser beams in the bank.

 

Example 1:


Input: bank = ["011001","000000","010100","001000"]
Output: 8
Explanation: Between each of the following device pairs, there is one beam. In total, there are 8 beams:
 * bank[0][1] -- bank[2][1]
 * bank[0][1] -- bank[2][3]
 * bank[0][2] -- bank[2][1]
 * bank[0][2] -- bank[2][3]
 * bank[0][5] -- bank[2][1]
 * bank[0][5] -- bank[2][3]
 * bank[2][1] -- bank[3][2]
 * bank[2][3] -- bank[3][2]
Note that there is no beam between any device on the 0th row with any on the 3rd row.
This is because the 2nd row contains security devices, which breaks the second condition.
Example 2:


Input: bank = ["000","111","000"]
Output: 0
Explanation: There does not exist two devices located on two different rows.
 

Constraints:

m == bank.length
n == bank[i].length
1 <= m, n <= 500
bank[i][j] is either '0' or '1'.
Accepted
60,760
Submissions
74,096
''')

