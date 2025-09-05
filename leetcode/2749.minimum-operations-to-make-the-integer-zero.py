from lc import *

# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/solutions/5823186/one-line-solution/?envType=daily-question&envId=2025-09-05

class Solution:
    def makeTheIntegerZero(self, v: int, u: int) -> int:
        return next((o for o in range(1,ceil(log2(max(v,v-60*u))+1)) if (q:=v-o*u).bit_count()<=o<=q),-1)

class Solution:
    def makeTheIntegerZero(self, v: int, u: int) -> int:
        return next((o for o in range(37)if(q:=v-o*u).bit_count()<=o<=q),-1)

test('''
2749. Minimum Operations to Make the Integer Zero
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given two integers num1 and num2.

In one operation, you can choose integer i in the range [0, 60] and subtract 2i + num2 from num1.

Return the integer denoting the minimum number of operations needed to make num1 equal to 0.

If it is impossible to make num1 equal to 0, return -1.

 

Example 1:

Input: num1 = 3, num2 = -2
Output: 3
Explanation: We can make 3 equal to 0 with the following operations:
- We choose i = 2 and subtract 22 + (-2) from 3, 3 - (4 + (-2)) = 1.
- We choose i = 2 and subtract 22 + (-2) from 1, 1 - (4 + (-2)) = -1.
- We choose i = 0 and subtract 20 + (-2) from -1, (-1) - (1 + (-2)) = 0.
It can be proven, that 3 is the minimum number of operations that we need to perform.
Example 2:

Input: num1 = 5, num2 = 7
Output: -1
Explanation: It can be proven, that it is impossible to make 5 equal to 0 with the given operation.
 

Constraints:

1 <= num1 <= 109
-109 <= num2 <= 109
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
11,551/37.6K
Acceptance Rate
30.7%
Topics
Bit Manipulation
Brainteaser
Enumeration
Weekly Contest 351
icon
Companies
Hint 1
If we want to make integer n equal to 0 by only subtracting powers of 2 from n, in how many operations can we achieve it?
Hint 2
We need at least - the number of bits in the binary representation of n, and at most - n.
Hint 3
Notice that, if it is possible to make num1 equal to 0, then we need at most 60 operations.
Hint 4
Iterate on the number of operations.
Similar Questions
Broken Calculator
Medium
Minimum Operations to Reduce X to Zero
Medium
''')
