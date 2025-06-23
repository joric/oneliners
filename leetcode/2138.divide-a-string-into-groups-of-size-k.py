from lc import *

# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/solutions/6861664/one-line-solution/?envType=daily-question&envId=2025-06-22

class Solution:
    def divideString(self, s: str, k: int, f: str) -> List[str]:
        return [*map(''.join,zip(*[iter(s+(k-len(s)%k)%k*f)]*k))]

class Solution:
    def divideString(self, s: str, k: int, f: str) -> List[str]:
        return [*map(''.join,zip_longest(*([iter(s)]*k),fillvalue=f))]

class Solution:
    def divideString(self, s: str, k: int, f: str) -> List[str]:
        return[s[i:i+k].ljust(k,f)for i in range(0,len(s),k)]

test('''
2138. Divide a String Into Groups of Size k
Solved
Easy
Topics
premium lock icon
Companies
Hint
A string s can be partitioned into groups of size k using the following procedure:

The first group consists of the first k characters of the string, the second group consists of the next k characters of the string, and so on. Each element can be a part of exactly one group.
For the last group, if the string does not have k characters remaining, a character fill is used to complete the group.
Note that the partition is done so that after removing the fill character from the last group (if it exists) and concatenating all the groups in order, the resultant string should be s.

Given the string s, the size of each group k and the character fill, return a string array denoting the composition of every group s has been divided into, using the above procedure.

 

Example 1:

Input: s = "abcdefghi", k = 3, fill = "x"
Output: ["abc","def","ghi"]
Explanation:
The first 3 characters "abc" form the first group.
The next 3 characters "def" form the second group.
The last 3 characters "ghi" form the third group.
Since all groups can be completely filled by characters from the string, we do not need to use fill.
Thus, the groups formed are "abc", "def", and "ghi".
Example 2:

Input: s = "abcdefghij", k = 3, fill = "x"
Output: ["abc","def","ghi","jxx"]
Explanation:
Similar to the previous example, we are forming the first three groups "abc", "def", and "ghi".
For the last group, we can only use the character 'j' from the string. To complete this group, we add 'x' twice.
Thus, the 4 groups formed are "abc", "def", "ghi", and "jxx".
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters only.
1 <= k <= 100
fill is a lowercase English letter.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
150,682/196K
Acceptance Rate
76.9%
Topics
String
Simulation
icon
Companies
Hint 1
Using the length of the string and k, can you count the number of groups the string can be divided into?
Hint 2
Try completing each group using characters from the string. If there aren’t enough characters for the last group, use the fill character to complete the group.
Similar Questions
Text Justification
Hard
Positions of Large Groups
Easy
''')
