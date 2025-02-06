from lc import *

# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        return reduce(lambda a,i:''.join(str(len(list(v)))+str(k) for k,v in groupby(a)),range(1,n),'1')

class Solution:
    def countAndSay(self, n: int) -> str:
        return reduce(lambda a,_:''.join(f'{len([*v])}{k}'for k,v in groupby(a)),range(1,n),'1')

class Solution:
    def countAndSay(self, n: int) -> str:
        a='1';[a:=''.join(f'{len([*v])}{k}'for k,v in groupby(a))for _ in[0]*~-n];return a

test('''
38. The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":


Given a positive integer n, return the nth term of the count-and-say sequence.

 

Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
 

Constraints:

1 <= n <= 30
''')