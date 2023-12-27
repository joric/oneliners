from lc import *

# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/discuss/4449328/wesimple-one-liner

class Solution:
    def minOperations(self, s: str) -> int:
        return min(sum(c==str((i+j)%2)for j,c in enumerate(s))for i in(0,1))

# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/discuss/4081867/Easy-solution-1-line

class Solution:
    def minOperations(self, s: str) -> int:
        return min(n:=sum(i%2==int(c)for i,c in enumerate(s)),len(s)-n)

# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/discuss/1064511/JavaC++Python-Easy-and-Concise/2152604

class Solution:
    def minOperations(self, s: str) -> int:
        return min(n:=sum(map(eq,s,cycle('01'))),len(s)-n)

test('''
1758. Minimum Changes To Make Alternating Binary String
Easy

589

21

Add to List

Share
You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

 

Example 1:

Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
Example 2:

Input: s = "10"
Output: 0
Explanation: s is already alternating.
Example 3:

Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".
 

Constraints:

1 <= s.length <= 10^4
s[i] is either '0' or '1'.
Accepted
39,898
Submissions
68,742
''')

