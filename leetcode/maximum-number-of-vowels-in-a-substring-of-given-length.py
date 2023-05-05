from lc import *

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        return (t:=[*accumulate(map(set('aeiou').__contains__,s),initial=0)]) and max(map(sub,t[k:],t))

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        return max(map(sub,(t:=[*accumulate(map(set('aeiou').__contains__,s),initial=0)])[k:],t))

test('''
1456. Maximum Number of Vowels in a Substring of Given Length
Medium

1739

64

Add to List

Share
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.
1 <= k <= s.length
Accepted
88,111
Submissions
147,102
Seen this question in a real interview before?

Yes

No
Keep a window of size k and maintain the number of vowels in it.
Keep moving the window and update the number of vowels while moving. Answer is max number of vowels of any window.
''')

