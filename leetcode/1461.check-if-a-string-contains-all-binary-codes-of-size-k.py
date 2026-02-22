from lc import *

# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/solutions/4016389/python-bitwise-manipulation-no-set-requi-q241/?envType=daily-question&envId=2026-02-23

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        m = 0
        t = 1 << k
        for i in range(len(s)-k+1):
            x = int(s[i:i+k],2)
            if x<t:
                m |= 1<<x
        return m==(1<<t)-1

# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/?envType=daily-question&envId=2026-02-23

class Solution(object):
    def hasAllCodes(self, s, k):
        return len(reduce(lambda a,i:(a.add(s[i:i+k]),a)[1],range(len(s)-k+1),set()))==2**k

# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/solutions/660655/python3-one-line-brute-force-by-ye15-qgat/?envType=daily-question&envId=2026-02-23

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return all(bin(i)[2:].zfill(k) in s for i in range(2**k))

# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/solutions/660610/python-1-line-by-auwdish-j17o/?envType=daily-question&envId=2026-02-23

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len({s[i:i+k]for i in range(len(s)-k+1)})==2**k

class Solution: # TLE
    def hasAllCodes(self, s: str, k: int) -> bool:
        return all(f'{i:0{k}b}'in s for i in range(1<<k))

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len({s[i:i+k]for i in range(len(s)-k+1)})==1<<k

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len({*zip(*[s[i:]for i in range(k)])})==1<<k

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return 0<len({*zip(*[s[i:]for i in range(k)])})>>k

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
