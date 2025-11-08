from lc import *

# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/discuss/877738/5-Line-Python-or-Simple-or-O(logn)

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        r = 0
        while n:
            r ^= n
            n //= 2
        return r

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        return next((r for _ in count()if not(n and(r:=r^n,n:=n//2))),r:=0)

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        return n^self.minimumOneBitOperations(n>>1) if n else 0

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        r=[0];exec('while n:\n r[0]^=n\n n//=2');return r[0]

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        return(f:=lambda r,n:n and f(r^n,n//2)or r)(0,n)

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        return(f:=lambda n:n and n^f(n//2))(n)

''' bonus cpp version (4 chars shorter)
class Solution {
public:
    int minimumOneBitOperations(int n) {
        int r=0;for(;n;n/=2)r^=n;return r;
    }
};
'''

test('''
1611. Minimum One Bit Operations to Make Integers Zero
Hard

442

364

Add to List

Share
Given an integer n, you must transform it into 0 using the following operations any number of times:

Change the rightmost (0th) bit in the binary representation of n.
Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.
Return the minimum number of operations to transform n into 0.

 

Example 1:

Input: n = 3
Output: 2
Explanation: The binary representation of 3 is "11".
"11" -> "01" with the 2nd operation since the 0th bit is 1.
"01" -> "00" with the 1st operation.
Example 2:

Input: n = 6
Output: 4
Explanation: The binary representation of 6 is "110".
"110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
"010" -> "011" with the 1st operation.
"011" -> "001" with the 2nd operation since the 0th bit is 1.
"001" -> "000" with the 1st operation.
 

Other examples:

Input: n = 9
Output: 14

Constraints:

0 <= n <= 10^9
Accepted
14,523
Submissions
22,882
''')