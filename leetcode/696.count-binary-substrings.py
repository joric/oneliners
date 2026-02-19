from lc import *

# https://leetcode.com/problems/count-binary-substrings/submissions/669717660/?envType=daily-question&envId=2026-02-19

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        return reduce(lambda a,x:(a[0]+min(a[1],x),x),(len([*g])for _,g in groupby(s)),(0,0))[0]

# https://leetcode.com/problems/count-binary-substrings/solutions/2343625/python-3-one-line-with-groupby-and-pairw-a09z/?envType=daily-question&envId=2026-02-19

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        return sum(starmap(min,pairwise(len(list(g))for _,g in groupby(s))))

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        return sum(map(min,t:=[len([*g])for _,g in groupby(s)],t[1:]))

# https://leetcode.com/problems/count-binary-substrings/solutions/7589047/one-line-solution-by-mikposp-jnvr/?envType=daily-question&envId=2026-02-19

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        return sum(map(min,pairwise(sum(1 for _ in g) for _,g in groupby(s))))

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        return sum(map(min,pairwise(map(len,s.replace('01','0 1').replace('10','1 0').split()))))

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        return sum(map(min,pairwise(len([*g])for _,g in groupby(s))))

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        return sum(map(min,pairwise(map(len,findall(r'0+|1+',s)))))

# POTD 2026-02-19

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        return sum(s.count('0'*i+'1'*i)+s.count('1'*i+'0'*i)for i in range(1,len(s)))

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        return sum(map(min,pairwise(map(len,findall('0+|1+',s)))))

test('''
696. Count Binary Substrings
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

 

Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
273,759/406.3K
Acceptance Rate
67.4%
Topics
Staff
Two Pointers
String
icon
Companies
Hint 1
How many valid binary substrings exist in "000111", and how many in "11100"? What about "00011100"?
Similar Questions
Encode and Decode Strings
Medium
Number of Substrings With Fixed Ratio
Medium
Count the Number of Substrings With Dominant Ones
Medium
''')
