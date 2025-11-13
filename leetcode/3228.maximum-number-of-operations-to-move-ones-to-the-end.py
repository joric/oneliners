from lc import *

# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/solutions/7341289/one-line-solution-by-mikposp-jlw1/?envType=daily-question&envId=2025-11-13

class Solution:
    def maxOperations(self, s: str) -> int:
        return sum(accumulate(map(len,findall('(1+)0',s))))

test('''
3228. Maximum Number of Operations to Move Ones to the End
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a binary string s.

You can perform the following operation on the string any number of times:

Choose any index i from the string where i + 1 < s.length such that s[i] == '1' and s[i + 1] == '0'.
Move the character s[i] to the right until it reaches the end of the string or another '1'. For example, for s = "010010", if we choose i = 1, the resulting string will be s = "000110".
Return the maximum number of operations that you can perform.

 

Example 1:

Input: s = "1001101"

Output: 4

Explanation:

We can perform the following operations:

Choose index i = 0. The resulting string is s = "0011101".
Choose index i = 4. The resulting string is s = "0011011".
Choose index i = 3. The resulting string is s = "0010111".
Choose index i = 2. The resulting string is s = "0001111".
Example 2:

Input: s = "00111"

Output: 0

 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
40,970/71.4K
Acceptance Rate
57.4%
Topics
String
Greedy
Counting
Weekly Contest 407
icon
Companies
Hint 1
It is optimal to perform the operation on the lowest index possible each time.
Hint 2
Traverse the string from left to right and perform the operation every time it is possible.
''')
