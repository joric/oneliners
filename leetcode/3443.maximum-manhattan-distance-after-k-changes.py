from lc import *

# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/solutions/6862033/two-simple-lines-of-code/?envType=daily-question&envId=2025-06-20

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        return max(min(int(abs(z.real)+abs(z.imag))+k*2,i+1)for i,z in enumerate(accumulate(1j**'ESWN'.find(c)for c in s)))

test('''
3443. Maximum Manhattan Distance After K Changes
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:

'N' : Move north by 1 unit.
'S' : Move south by 1 unit.
'E' : Move east by 1 unit.
'W' : Move west by 1 unit.
Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.

Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.

The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.
 

Example 1:

Input: s = "NWSE", k = 1

Output: 3

Explanation:

Change s[2] from 'S' to 'N'. The string s becomes "NWNE".

Movement    Position (x, y) Manhattan Distance  Maximum
s[0] == 'N' (0, 1)  0 + 1 = 1   1
s[1] == 'W' (-1, 1) 1 + 1 = 2   2
s[2] == 'N' (-1, 2) 1 + 2 = 3   3
s[3] == 'E' (0, 2)  0 + 2 = 2   3
The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.

Example 2:

Input: s = "NSWWEW", k = 3

Output: 6

Explanation:

Change s[1] from 'S' to 'N', and s[4] from 'E' to 'W'. The string s becomes "NNWWWW".

The maximum Manhattan distance from the origin that can be achieved is 6. Hence, 6 is the output.

Other examples:

Input: s = "WS", k = 0
Output: 2

Constraints:

1 <= s.length <= 105
0 <= k <= s.length
s consists of only 'N', 'S', 'E', and 'W'.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
16,601/52.8K
Acceptance Rate
31.4%
Topics
Hash Table
Math
String
Counting
icon
Companies
Hint 1
We can brute force all the possible directions (NE, NW, SE, SW).
Hint 2
Change up to k characters to maximize the distance in the chosen direction.
Similar Questions
As Far from Land as Possible
Medium
''')
