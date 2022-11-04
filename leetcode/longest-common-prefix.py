from lc import *

class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return os.path.commonprefix(strs)

class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return strs[0][:len([*takewhile(lambda c:len(set(c))==1,zip(*strs))])]

class Solution3:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a,b = min(strs), max(strs)
        for i, c in enumerate(a):
            if c != b[i]:
                return a[:i]
                break
        return a

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return (lambda a,b:a[:next((i for i,c in enumerate(a) if c!=b[i]),len(a))])(min(strs),max(strs))

test('''

14. Longest Common Prefix
Easy

11115

3498

Add to List

Share
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

''')