from lc import *

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return ''.join(sorted(str(n))) in set(["1", "2", "4", "8", "16", "23", "46", "128", "256", "125", "0124", "0248", "0469", "1289", "13468", "23678", "35566", "011237", "122446", "224588", "0145678", "0122579", "0134449", "0368888", "11266777", "23334455", "01466788", "112234778", "234455668", "012356789", "0112344778"])

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return any(sorted(str(n))==sorted(str(1<<i))for i in range(30))

# POTD 2025-08-10

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s=sorted;return any(s(str(n))==s(str(1<<i))for i in range(30))

test('''
869. Reordered Power of 2
Medium

1931

394

Add to List

Share
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

 

Example 1:

Input: n = 1
Output: true
Example 2:

Input: n = 10
Output: false

Other examples:

Input: n = 46
Output: True

Input: n = 1521
Output: False

Constraints:

1 <= n <= 10^9
''')
