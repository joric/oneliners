from lc import *

# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/discuss/427565/Python-one-line-solution-using-Counter

class Solution:
    def countCharacters(self, w: List[str], c: str) -> int:
        return sum(map(len,filter(lambda s:not Counter(s)-Counter(c),w)))

# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/discuss/896268/Python-slow-one-liner

class Solution:
    def countCharacters(self, w: List[str], c: str) -> int:
        return sum(len(s)for s in w if not Counter(s)-Counter(c))

# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/discuss/361377/Python-concise-1-liner

class Solution:
    def countCharacters(self, w: List[str], c: str) -> int:
        return sum(len(s) for s in w if Counter(s)<Counter(c))

class Solution:
    def countCharacters(self, w: List[str], c: str) -> int:
        f=Counter;return sum(len(s)*(f(s)<=f(c))for s in w)

# still passes tests with < missing test ["a"] "a"

class Solution:
    def countCharacters(self, w: List[str], c: str) -> int:
        f=Counter;return sum(len(s)*(f(s)<f(c))for s in w) 

test('''
1160. Find Words That Can Be Formed by Characters
Easy

1484

159

Add to List

Share
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.
Accepted
165,152
Submissions
243,632
''')
