from lc import *

# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/discuss/3552978/Python3-1-line-bitwise-operation-with-step-by-step-explanation

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return (bin(~(c|(~a)))+bin(~(c|(~b)))+bin(c&(~(a|b)))).count('1')

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return bin((a|b)^c).count('1')+bin((a&b)&~c).count('1')

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return (bin((a|b)^c)+bin(a&b&((a|b)^c))).count("1")

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return (c^(a|b)).bit_count()+(a&b&~c).bit_count()

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return sum(map(int.bit_count,(a&b&~c,c^(a|b))))

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return ((c^(a|b))|((a&b&~c)<<32)).bit_count()

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return (bin(c^(a|b))+bin(a&b&~c)).count("1")

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return (c^(a|b)|(a&b&~c)<<32).bit_count()

test('''
1318. Minimum Flips to Make a OR b Equal to c
Medium

642

47

Add to List

Share
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

 

Example 1:



Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
Example 2:

Input: a = 4, b = 2, c = 7
Output: 1
Example 3:

Input: a = 1, b = 2, c = 3
Output: 0
 

Constraints:

1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9
Accepted
31,741
Submissions
47,980
Seen this question in a real interview before?

Yes

No
Check the bits one by one whether they need to be flipped.
''')

