from lc import *

# https://leetcode.com/problems/find-common-characters

class Solution:
    def commonChars(self, w: List[str]) -> List[str]:
        return reduce(and_,map(Counter,w)).elements()

test('''
1002. Find Common Characters
Easy

3497

298

Add to List

Share
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
Accepted
214,377
Submissions
310,814
''')