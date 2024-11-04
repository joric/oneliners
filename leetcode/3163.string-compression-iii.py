from lc import *

# https://leetcode.com/problems/string-compression-iii/discuss/5210766/Python-one-line

class Solution:
    def compressedString(self, word: str) -> str:
        return ''.join((lambda s: ''.join(''.join(str(len(s[i:i+9])) + c) for i in range(0, len(s), 9)))(''.join(list(g))) for c, g in groupby(word))

class Solution:
    def compressedString(self, w: str) -> str:
        return''.join((lambda c,s:''.join(f'{len(s[i:i+9])}{c}'for i in range(0,len(s),9)))(c,[*g])for c,g in groupby(w))

# python 3.12 only because of batched
class Solution:
    def compressedString(self, w: str) -> str:
        return''.join(f'{len(s)}{c}'for c,g in groupby(w)for s in batched([*g],9))

# https://leetcode.com/problems/string-compression-iii/discuss/5484717/Ease-andand-Short-one-line
# js: var compressedString = (word) => word.replace(/(.)\1{0,8}/g, (str, s) => `${str.length}${s}`);

class Solution:
    def compressedString(self, w: str) -> str:
        return re.sub(r'(.)\1{0,8}',lambda m:f'{len(m[0])}{m[1]}',w)

class Solution:
    def compressedString(self, w: str) -> str:
        return re.sub(r'(.)\1{,8}',lambda m:f'{len(m[0])}'+m[1],w)

test('''
3163. String Compression III
Medium

119

9

Add to List

Share
Given a string word, compress it using the following algorithm:

Begin with an empty string comp. While word is not empty, use the following operation:
Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
Append the length of the prefix followed by c to comp.
Return the string comp.

 

Example 1:

Input: word = "abcde"

Output: "1a1b1c1d1e"

Explanation:

Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c", "d", and "e" as the prefix in each operation.

For each prefix, append "1" followed by the character to comp.

Example 2:

Input: word = "aaaaaaaaaaaaaabb"

Output: "9a5a2b"

Explanation:

Initially, comp = "". Apply the operation 3 times, choosing "aaaaaaaaa", "aaaaa", and "bb" as the prefix in each operation.

For prefix "aaaaaaaaa", append "9" followed by "a" to comp.
For prefix "aaaaa", append "5" followed by "a" to comp.
For prefix "bb", append "2" followed by "b" to comp.
 

Constraints:

1 <= word.length <= 2 * 105
word consists only of lowercase English letters.
Accepted
41,816
Submissions
74,557
''')
