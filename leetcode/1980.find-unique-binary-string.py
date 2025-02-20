from lc import *

# https://leetcode.com/problems/find-unique-binary-string/discuss/1493853/Python-one-line-easy-to-understand-list-comprehension

'''
This uses Cantor's diagonal argument - a clever mathematical trick that guarantees we'll get a string different from all strings in the input list.

Let's see how it works:

Example 1: ["01","10"]
Position 0: "01" -> take opposite of 0 -> "1"
Position 1: "10" -> take opposite of 0 -> "1"
Result: "11"

Example 2: ["00","01"]
Position 0: "00" -> take opposite of 0 -> "1"
Position 1: "01" -> take opposite of 1 -> "0"
Result: "11"

Example 3: ["111","011","001"]
Position 0: "111" -> take opposite of 1 -> "0"
Position 1: "011" -> take opposite of 1 -> "0"
Position 2: "001" -> take opposite of 1 -> "0"
Result: "101"
'''

class Solution:
    def findDifferentBinaryString(self, a: List[str]) -> str:
        return next(filterfalse(a.__contains__,map(''.join,product(*['01']*len(a)))))

class Solution:
    def findDifferentBinaryString(self, a: List[str]) -> str:
        return''.join(str(int(x[i]=='0'))for i,x in enumerate(a))

class Solution:
    def findDifferentBinaryString(self, a: List[str]) -> str:
        return''.join(str(1^int(x[i]))for i,x in enumerate(a))

class Solution:
    def findDifferentBinaryString(self, a: List[str]) -> str:
        return''.join('10'[n[i][i]>'0']for i in range(len(a)))

class Solution:
    def findDifferentBinaryString(self, a: List[str]) -> str:
        return''.join('10'[x[i]>'0']for i,x in enumerate(a))

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

Other examples:

Input: nums = ["000","001","110"]
Output: "010"

Input: nums = ["10","11"]
Output: "00"

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
''',check=lambda r,e,a:len(r)==len(a[0])and r not in a)
