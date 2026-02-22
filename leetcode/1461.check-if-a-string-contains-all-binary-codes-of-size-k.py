from lc import *

# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len({*zip(*[s[i:]for i in range(k)])})>>k>0

test('''
1461. Check If a String Contains All Binary Codes of Size K
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

 

Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
Example 2:

Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
Example 3:

Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and does not exist in the array.


Other examples:

Input: s = "00110110", k = 2
Output: true

Constraints:

1 <= s.length <= 5 * 105
s[i] is either '0' or '1'.
1 <= k <= 20
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
140,468/246.8K
Acceptance Rate
56.9%
Topics
Senior
Hash Table
String
Bit Manipulation
Rolling Hash
Hash Function
Biweekly Contest 27
icon
Companies
Hint 1
We need only to check all sub-strings of length k.
Hint 2
The number of distinct sub-strings should be exactly 2^k.
''')
