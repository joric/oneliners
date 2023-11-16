from lc import *

# https://leetcode.com/problems/find-unique-binary-string/discuss/1493853/Python-one-line-easy-to-understand-list-comprehension

class Solution:
    def findDifferentBinaryString(self, n: List[str]) -> str:
        return''.join(str(int(x[i]=='0'))for i,x in enumerate(n))

class Solution:
    def findDifferentBinaryString(self, n: List[str]) -> str:
        return''.join(str(1^int(x[i]))for i,x in enumerate(n))

class Solution:
    def findDifferentBinaryString(self, n: List[str]) -> str:
        return''.join('10'[x[i]=='1']for i,x in enumerate(n))

test('''
1980. Find Unique Binary String
Medium

1176

48

Add to List

Share
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
 

Constraints:

n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.
Accepted
53,822
Submissions
78,354
''',check=lambda r,e,n:len(r)==len(n[0])and r not in n)

