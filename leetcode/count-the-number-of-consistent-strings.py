from lc import *

# https://leetcode.com/problems/count-the-number-of-consistent-strings/discuss/969548/Python-1-line

class Solution:
    def countConsistentStrings(self, a: str, w: List[str]) -> int:
        return sum(all(c in a for c in s)for s in w)

# https://leetcode.com/problems/count-the-number-of-consistent-strings/discuss/1019418/Python-3-one-line-solution

class Solution:
    def countConsistentStrings(self, a: str, w: List[str]) -> int:
        return sum(s.issubset(a) for s in map(set,w))

# https://leetcode.com/problems/count-the-number-of-consistent-strings/discuss/4035909/One-line-solution

class Solution:
    def countConsistentStrings(self, a: str, w: List[str]) -> int:
        return sum(not({*s}-{*a})for s in w)

test('''
1684. Count the Number of Consistent Strings
Easy

1727

74

Add to List

Share
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

 

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
 

Constraints:

1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters.
Accepted
190,942
Submissions
228,305
''')
